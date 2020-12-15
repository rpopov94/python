from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from weather import smart_function


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
request = ''

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне название города!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Этот бот предоставляет актуальные данные о погоде," \
                        "если не плучается найти город, введите название на латинице")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def do_answer(mes: types.Message):
    text = mes.text
    if text and not text.startswith('/'):
        await mes.reply(text=smart_function(text), reply=False)


if __name__ == '__main__':
    executor.start_polling(dp)