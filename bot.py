import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from weather import ob_havo_qidir
from regionbutton import viloyatlar_btn

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7725039127:AAHDQ2nKCuxnzLy5OT-BXBSGrx3h33ighyI")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom, {full_name}",reply_markup=viloyatlar_btn)

@dp.message(F.text)
async def ob_havo_malumoti(message: types.Message):
    shaxar = message.text
    result = ob_havo_qidir(shaxar)
    await message.reply(text=result)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())