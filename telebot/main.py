from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config
import weather

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне название города!\nДля получения справки введите\n/help")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Этот бот предоставляет актуальные данные о погоде,\n" \
                        "если не плучается найти город,\n "
                        "введите название на латинице\n" \
                        "для получение истории\n" \
                        "[город] -h [yyyy-mm-dd]\n" \
                        "Прогноз погоды на 3 дня\n" \
                        "[город] -f\n" \
                        "Текущая погода\n" \
                        "[город]", \
                        reply=False
                        )


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def do_answer(mes: types.Message):
    text = mes.text
    if text and not text.startswith('/'):
        await mes.reply(text=weather.smart_function(text), reply=False)


if __name__ == '__main__':
    executor.start_polling(dp)