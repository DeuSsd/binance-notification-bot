import asyncio
import json
from pathlib import Path
from typing import Dict
# import websocket

from .trigers import MarketSensor
import websocket
import rel
#
# BASE_URL = 'wss://fstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice'
BASE_URL = 'wss://fstream.binance.com/stream?streams='


# websocket.enableTrace(True)

class Worker:
    def __init__(self, token: str, token_config: Dict[str, str], queue: asyncio.Queue) -> None:
        self.token_title = token
        self.token = token.replace('/', '').lower()
        self.queue: asyncio.Queue = queue
        self.url = f"{BASE_URL}{self.token}@markPrice"

        trigger_type = token_config.get("trigger")
        trigger_price = token_config.get("price")
        self.marketSensor = MarketSensor(
            self.token, trigger_type, trigger_price)

        self.wsapp = self.subscribe(self.url)

    def subscribe(self, url: str) -> websocket.WebSocketApp:
        return websocket.WebSocketApp(
            url,
            # on_open=self.on_open,
            on_message=self.on_message,
            # on_close=self.on_close
        )

    def run_forever(self):
        self.wsapp.run_forever(dispatcher=rel)

    # @staticmethod
    # def on_open(ws):
    #     ws.send(f"connected")

    def on_message(self, ws, message):
        msg = json.loads(message)
        data = msg.get('data')
        price = data.get('p')

        if self.marketSensor.trigger(float(price)):
            msg = f"Pair {self.token_title} was triggered: {price} {self.marketSensor.trigger_type} {self.marketSensor.trigger_price}"
            print("generate", msg, f'ОЧЕРЕДЬ {self.queue.qsize()}')
            self.queue.put_nowait(msg)

    # def owner(self, function):
    #     def inner(*args, **kwargs):

    #         function(*args, **kwargs)
    #     return inner
    # @staticmethod
    # def on_close(ws, close_status_code, close_msg):
    #     print(">>>>>>CLOSED")


if __name__ == "__main__":
    pass
