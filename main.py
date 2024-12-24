import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Была команда старт")


# @dp.message()
# async def slon(message: types.Message):
#     if message.text == "Утро":
#         await message.answer("Пьем кофэ")


# @dp.message()
# async def slon(message: types.Message):
#     if message.text == "День":
#         await message.answer("Ем супчик")


@dp.message()
async def slon(message: types.Message):
    if message.text == "Вечер":
        await message.answer("Пью чай")
    else:
        await message.answer(message.text)


# @dp.message()
# async def echo(message: types.Message):
#     await message.answer("Напиши что то умное!")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
