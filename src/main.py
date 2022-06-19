import rel
from datetime import datetime
from services.tgbot.app import bot, send_notifications
from websocket._exceptions import WebSocketConnectionClosedException
import threading
import asyncio

from pathlib import Path
from services.tools.configTools import load_config
from services.binance.worker import Worker

from rich.traceback import install
install(show_locals=True)  # show readable Traceback when exception

binance_config_path = Path("src/services/binance/config/config.json")
bnc = load_config(binance_config_path)


#TODO Подумать как переделать, наверняка можно переоткрывать закрытое соедиение

def workers_dataminers_running_forever(queue):
    while True:
        thread_workers_dataminers = threading.Thread(target=workers_dataminers_loop, args=(queue,))
        thread_workers_dataminers.start()
        thread_workers_dataminers.join()
        

def workers_dataminers_loop(queue):
    try:
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

        # rel.signal(2, rel.abort)  # Keyboard Interrupt
        # print("patch")
        rel.dispatch()
        print("dispatched")
        #TODO через 5 минут соединение падает, закрывает binance, почему не переоткрывается?
    except WebSocketConnectionClosedException as e:
        print(e)
        pass
    except e:
        print(e)
        pass


async def notify_worker(queue):
    while True:
        msg_notify = await queue.get()
        await send_notifications(msg_notify)
        # print(msg_notify)
        queue.task_done()


async def bot_notification_loop(queue):
    tasks = []
    tasks.append(asyncio.create_task(notify_worker(queue)))
    tasks.append(asyncio.create_task(bot.infinity_polling()))
    await asyncio.gather(*tasks)


# def bot_notification_loop_running_forever(queue):
#     while True:
#         thread_workers_dataminers = threading.Thread(target=main, args=(queue,))
#         thread_workers_dataminers.start()
#         thread_workers_dataminers.join()
        

def main(queue):
    asyncio.run(bot_notification_loop(queue))


if __name__ == "__main__":
    queue = asyncio.Queue()
    thread_dataminers = threading.Thread(target=workers_dataminers_running_forever, args=(queue,))
    # thread_tgbot = threading.Thread(target=main, args=(queue,))
    # thread_tgbot.start()
    thread_dataminers.start()
    # thread_websocket2.start()
    # workers_loop(queue)
    # workers_dataminers_loop(queue)
    # bot_notification_loop_running_forever(queue)
    main(queue)
