import asyncio
import json
from typing import Dict

from .trigers import MarketSensor
import websocket
import rel
#
# BASE_URL = 'wss://fstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice'
BASE_URL = 'wss://fstream.binance.com/stream?streams='


# websocket.enableTrace(True)

# TODO добавить delay?
class Worker:
    def __init__(self, token: str, token_config: Dict[str, str], queue: asyncio.Queue) -> None:
        assert isinstance(
            token, str), "Expected value type {type(str)}, but got {type(token)}"
        self.token_title = token
        self.token = token.replace('/', '').lower()
        assert isinstance(
            queue, asyncio.Queue), "Expected value type {type(asyncio.Queue)}, but got {type(queue)}"
        self.queue: asyncio.Queue = queue

        # self.url = f"{BASE_URL}{self.token}@markPrice@1s"
        self.url = f"{BASE_URL}{self.token}@markPrice" # per 3 sec
        assert isinstance(
            token_config, dict), "Expected value type {type(dict)}, but got {type(token_config)}"
        assert 'trigger' in token_config, "Expected key 'token_config' not found"
        assert 'price' in token_config, "Expected key 'token_config' not found"
        trigger_type = token_config.get("trigger")
        trigger_price = token_config.get("price")
        self.marketSensor = MarketSensor(
            self.token, trigger_type, trigger_price)
        self.wsapp = self.subscribe(self.url)

    def subscribe(self, url: str) -> websocket.WebSocketApp:

        return websocket.WebSocketApp(
            url,
            on_message=self.on_message,
        )
        
    # def subscribe(self, url: str):
    #     return websocket.WebSocketApp(
    #         url,
    #         # on_open=self.on_open,
    #         on_message=self.on_message,
    #         # on_close=self.on_close
    #     )

    def run_forever(self):
        self.wsapp.run_forever(dispatcher=rel)

    def on_message(self, ws, message):
        msg = json.loads(message)
        print(msg)
        data = msg.get('data')
        price = data.get('p')

        if self.marketSensor.trigger(float(price)):
            msg = f"Pair {self.token_title} was triggered: {price} {self.marketSensor.trigger_type} {self.marketSensor.trigger_price}"
            # print("generate", msg, f'ОЧЕРЕДЬ {self.queue.qsize()}')
            self.queue.put_nowait(msg)


if __name__ == "__main__":
    # queue = asyncio.Queue()
    # worker = Worker('BTC/USDT',{"trigger":'less', 'price': '40000'},queue)
    pass
