from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from weather import get_weather


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне название города!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Этот бот предоставляет актуальные данные о погоде")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_weather(msg.text))


if __name__ == '__main__':
    executor.start_polling(dp)