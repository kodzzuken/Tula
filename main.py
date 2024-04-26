from random import choice
from time import time
from aiogram import executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types
from config import TOKEN_API
from command import dp
from db.db import db_start, db_deader

async def on_startup(_):
    print("Здравствуйте!")


@dp.message_handler()
async def echo_upper(message: types.Message):
    # print(message.reply_to_message['from'])
#так тоша будь другом  кругом, напиши тут код который будет проверять айдишник пользователя по базе данных

if __name__ == '__main__':
    print('hello world')
    db_deader()

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
