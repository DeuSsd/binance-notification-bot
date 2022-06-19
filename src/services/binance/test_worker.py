import unittest
import asyncio
import queue as q  # syncronized queue class
import websocket
from .worker import Worker


class TestSocket(unittest.TestCase):
    def test_empty_initialization(self):
        queue = asyncio.Queue()

        with self.assertRaises(AssertionError):
            worker = Worker(2, {"trigger": 'less', 'price': '123'}, queue)
        with self.assertRaises(AssertionError):
            worker = Worker('tokenName', {}, queue)
        with self.assertRaises(AssertionError):
            worker = Worker(
                'tokenName', {"trigggger": 'less', 'price': '123'}, queue)
        with self.assertRaises(AssertionError):
            worker = Worker(
                'tokenName', {"trigggger": 'less', 'price': '123'}, 'queue')
        with self.assertRaises(AssertionError):
            worker = Worker(
                'tokenName', {"trigggger": 'less', 'price': '123'}, q.Queue())

    def test_worker_connection(self):
        queue = asyncio.Queue()
        worker = Worker(
            'BTC/USDT', {"trigger": 'less', 'price': '40000'}, queue)
        self.assertTrue(isinstance(worker.wsapp, websocket.WebSocketApp))


if __name__ == '__main__':
    unittest.main()
