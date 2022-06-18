#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from os import environ
from pathlib import Path

from .tools.configTools import load_config
from . import blogic as bl 
# from time import sleep
# from telebot import TeleBot
# import telebot
from telebot.async_telebot import AsyncTeleBot






_load_env = lambda config_data_dict, ENV_KEY: config_data_dict.get(ENV_KEY) if ENV_KEY not in environ.keys() else environ[ENV_KEY]


api_token_path = Path('token\\telegram\\token.json')
API_TOKEN = _load_env(load_config(api_token_path), "TOKEN")

# bot = TeleBot(API_TOKEN)
bot = AsyncTeleBot(API_TOKEN)
print(API_TOKEN)

# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     msg =  """\
# Данный бот предназначен для выбора Красавчика дня!
# Доступные команды:
# - /enable - Включить нотификации
# - /disable - Выключить нотификации
# """
#     bot.send_message(message.chat.id, msg, disable_notification=True)

# @bot.message_handler(commands=['enable'])
# def run_the_game(message):
#     chat_id = message.chat.id
#     status = bl.enable_notification(chat_id)
#     if status:
#         bot.send_message(chat_id, "Уведомления включены")
        

# @bot.message_handler(commands=['disable'])
# def run_the_game(message):
#     chat_id = message.chat.id
#     status = bl.disable_notification(chat_id)
#     if status:
#         bot.send_message(chat_id, "Уведомления выключены")
        
        
# def send_notifications(msg):
#     list_chat_id = bl.collect_chat_for_notificate()
#     for chat_id in list_chat_id:
#         bot.send_message(chat_id, msg)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
# async def send_welcome(message: telebot.types.Message):
async def send_welcome(message):
    msg =  """\
Данный бот предназначен для выбора Красавчика дня!
Доступные команды:
- /enable - Включить нотификации
- /disable - Выключить нотификации
"""
    await bot.send_message(message.chat.id, msg, disable_notification=True)


@bot.message_handler(commands=['enable'])
async def run_the_game(message):
    chat_id = message.chat.id
    status = bl.enable_notification(chat_id)
    if status:
        await bot.send_message(chat_id, "Уведомления включены")
        

@bot.message_handler(commands=['disable'])
async def run_the_game(message):
    chat_id = message.chat.id
    status = bl.disable_notification(chat_id)
    if status:
        await bot.send_message(chat_id, "Уведомления выключены")
        
        
async def send_notifications(msg):
    list_chat_id  = bl.collect_chat_for_notificate()
    for chat_id in list_chat_id:
        print(chat_id, msg )
        await bot.send_message(chat_id, msg)





