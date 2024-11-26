import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7887208020:AAG4pV1eZZg3I9L7rB9P2CjapgGhaQxGdic'
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Alen хач, любит тасю!")



@dp.message()
async def echo(message: types.Message):
    await message.answer("Сам ты осел глупый!")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
