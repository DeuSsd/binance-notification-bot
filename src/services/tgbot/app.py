#!/usr/bin/python

from os import environ
from pathlib import Path

from .tools.configTools import load_config
from . import blogic as bl 
# from telebot import TeleBot
# import telebot
from telebot.async_telebot import AsyncTeleBot






_load_env = lambda config_data_dict, ENV_KEY: config_data_dict.get(ENV_KEY) if ENV_KEY not in environ.keys() else environ[ENV_KEY]


api_token_path = Path('token\\telegram\\token.json')
API_TOKEN = _load_env(load_config(api_token_path), "TOKEN")

# bot = TeleBot(API_TOKEN)
bot = AsyncTeleBot(API_TOKEN)
# print(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
# async def send_welcome(message: telebot.types.Message):
async def send_welcome(message):
    msg =  """\
Данный бот предназначен для получения уведомлений о сработанных тригерах!
Доступные команды:
- /enable - Включить нотификации
- /disable - Выключить нотификации
"""
    await bot.send_message(message.chat.id, msg, disable_notification=True)


@bot.message_handler(commands=['enable'])
async def enable_notification(message):
    chat_id = message.chat.id
    status = bl.enable_notification(chat_id)
    if status:
        await bot.send_message(chat_id, "Уведомления включены")
        

@bot.message_handler(commands=['disable'])
async def disable_notification(message):
    chat_id = message.chat.id
    status = bl.disable_notification(chat_id)
    if status:
        await bot.send_message(chat_id, "Уведомления выключены")
        
        
async def send_notifications(msg):
    list_chat_id  = bl.collect_chat_for_notificate()
    for chat_id in list_chat_id:
        # print(chat_id, msg )
        await bot.send_message(chat_id, msg)





