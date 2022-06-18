
import asyncio
import json
from websockets import connect


class WebsocketAPI():
    def __init__(self, url) -> None:
        self.url = url

    async def __aenter__(self):
        self._connection = connect(self.url)
        self.websocket = await self._connection.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._connection.__aexit__(*args, **kwargs)


    async def send(self, message):
        await self.websocket.send(message)
        
    async def recieve(self):
        return await self.websocket.recv()
    
    
    
async def main():
    BASE_URL = 'wss://fstream.binance.com:443'
    ws = WebsocketAPI(BASE_URL)
    
    data = {
        "method": "SUBSCRIBE",
        "params":
        [
        "btcusdt@MarkPrice",
        ],
        "id": 1
        }
    
    async with WebsocketAPI(BASE_URL) as ws:
        await ws.send(json.dumps(data))
        # while True:
        print(json.loads(await ws.recieve()))
            
    
if __name__ == "__main__":
    #  loop = asyncio.get_event_loop()
    # loop.run_until_complete(main()
   asyncio.run(main())
        