from datetime import datetime
from services.tgbot.app import bot, send_notifications

import threading
import asyncio

from pathlib import Path
from services.tools.configTools import load_config
from services.binance.worker import Worker

binance_config_path = Path("src\\services\\binance\\config\\config.json")
bnc = load_config(binance_config_path)

print(bnc)

import rel



from rich.traceback import install
install(show_locals=True)

    
# for worker in Workers:
#     # Calling the function `marketSensortrigger` with the argument `10`
#     print(worker.marketSensor.trigger(10))

async def notify_worker(queue):
    while True:
        msg_notify = await queue.get()
        await send_notifications(msg_notify)
        queue.task_done()


def workers_loop(queue):
    Workers = []
    for token_title, token_config in bnc.items():
        Workers.append(Worker(
            token=token_title,
            token_config=token_config,
            queue=queue))

    for worker in Workers:
        print(worker.marketSensor)
        
    for worker in Workers:
        worker.run_forever()
        
        
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

async def bot_loop(queue):
    tasks = []
    # 

    # for worker in Workers:
    #     worker.run_forever()
        
   
    print("ss")
    tasks.append(asyncio.create_task(notify_worker(queue)))
    print("ss")
    # tasks.append(asyncio.create_task(qapp(queue)))
    # print("ss")
    tasks.append(asyncio.create_task(bot.infinity_polling()))
    print("ss")
    await asyncio.gather(*tasks)
    

def t_main(queue):
    asyncio.run(bot_loop(queue))

async def main():
    queue = asyncio.Queue()
    
   
    
    tasks = []
    # 

    # for worker in Workers:
    #     worker.run_forever()
        
   
    print("ss")
    tasks.append(asyncio.create_task(notify_worker(queue)))
    # tasks.append(asyncio.create_task(qapp(queue)))
    # print("ss")
    tasks.append(asyncio.create_task(bot.infinity_polling()))
    print("ss")
    await asyncio.gather(*tasks)
    print("ss")


async def qapp(query):
    await asyncio.sleep(1)
    print("w2we ",datetime.now())
    for _ in range(10):
        query.put_nowait(f"{datetime.now()}")
    print("wewe ",datetime.now())

if __name__ == "__main__":
    queue = asyncio.Queue()
    
    # thread_websocket = threading.Thread(target=workers_loop, args=(queue,))
    thread_websocket2 = threading.Thread(target=t_main, args=(queue,))
    # thread_websocket.start()
    thread_websocket2.start()
    workers_loop(queue)
    
    # t_main(queue)
    # asyncio.run(main())
    
    