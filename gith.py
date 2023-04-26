import logging

from aiogram import types, Bot, Dispatcher, executor


bot = Bot(token='5942679802:AAFpR58M3nIuqlm9zxQd5o_3t8-7ID_IYLE')

logging.basicConfig(level = logging.INFO)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    return SendMessage(message.chat.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)