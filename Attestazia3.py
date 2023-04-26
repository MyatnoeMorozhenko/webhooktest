#Реализовать бота, приветствующего пользователя при вводе команды /start
# и выводящего информацию о себе при вводе команды /about.

#для вебхука
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(token='5942679802:AAFpR58M3nIuqlm9zxQd5o_3t8-7ID_IYLE')

WEBHOOK_HOST = 'https://601b-2a02-2168-ac63-9900-442-eadb-74e8-8047.eu.ngrok.io' #адрес сервера
WEBHOOK_PATH = '' #путь до апи
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}' #адрес, на который принимаются запросы

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = 3001

logging.basicConfig(level = logging.INFO)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    return SendMessage(message.chat.id, message.text)

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup = on_startup,
        on_shutdown= on_shutdown,
        skip_updates= True,
        host = WEBHOOK_HOST,
        port = WEBAPP_PORT
    )



""""
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='6031505242:AAG5h91bzXepwnptx_IMeEGu-oH0HQdlUPU')
dp = Dispatcher(bot)

b1 = InlineKeyboardButton('Да', callback_data='button1')
b2 = InlineKeyboardButton('Нет', callback_data='button2')

keyb_client = InlineKeyboardMarkup().add(b1).add(b2)

@dp.message_handler(commands = ['start'])
async def start_bot(msg: types.Message):
    await bot.send_message(msg.from_user.id,f'Привет,{msg.from_user.full_name} !', reply_markup=keyb_client)

@dp.message_handler(commands = ['about'])
async def about_bot(msg: types.Message):
    await bot.send_message(msg.from_user.id,'Я бот для изучения английского языка. Помогу тебе поднять уровень, обновить знания и практиковать свои коммуникативные навыки.')

@dp.callback_query_handler(lambda c: True)
async def agree(callback_query: types.CallbackQuery):
    if callback_query.data == 'button1':
        await callback_query.message.edit_text('Вы нажали на кнопку "ДА', reply_markup = keyb_client)
    elif callback_query.data == 'button2':
        await callback_query.message.edit_text('Вы нажали на кнопку "НЕТ', reply_markup=keyb_client)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) """