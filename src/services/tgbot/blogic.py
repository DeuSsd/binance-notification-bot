

from .models.models import *

from peewee import ModelSelect


from typing import Callable, List, Optional, TypeVar
id = TypeVar('id')


def _create_notification(chat_id: id) -> Config:
    new_chat_config = Config(
        chat_id=chat_id,
    )
    new_chat_config.save()
    return new_chat_config


def enable_notification(chat_id: id) -> bool:
    query = Config.select().where(
        (Config.chat_id == chat_id)
    )
    if not len(query):
        _create_notification(chat_id)
        return True
    else:
        assert len(query) == 1, "There are dublicates in table"
        selected_chat_config: Config = query[0]
        _change_status_notification(selected_chat_config, True)
        return True


def disable_notification(chat_id: id) -> bool:
    query = Config.select().where(
        (Config.chat_id == chat_id)
    )
    if len(query):
        assert len(query) == 1, "There are dublicates in table"
        selected_chat_config: Config = query[0]
        _change_status_notification(selected_chat_config, False)
        return True
    return False


def _change_status_notification(selected_chat_config: Config, status: bool) -> Config:
    selected_chat_config.status = status
    selected_chat_config.save()
    return selected_chat_config


def change_delay_notification(chat_id: id, delay: int) -> bool:
    query = Config.select().where(
        (Config.chat_id == chat_id)
    )
    if len(query):
        assert len(query) == 1, "There are dublicates in table"
        selected_chat_config: Config = query[0]
        selected_chat_config.delay = delay
        selected_chat_config.save()
    return True


def collect_chat_for_notificate() -> list:
    query = Config.select(Config.chat_id).where(
        (Config.status == True)
    )
    return [item.chat_id for item in query]


#TODO Выделить в отельную функцию _collback()?
# def find_execute(chat_id: id, function: Callable):
#     query = Config.select().where(
#         (Config.chat_id == chat_id)
#     )
#     if len(query):
#         assert len(query) == 1, "There are dublicates in table"
#         selected_chat_config: Config = query[0]
        
        
#         selected_chat_config.delay = delay
#         selected_chat_config.save()
#     return True


