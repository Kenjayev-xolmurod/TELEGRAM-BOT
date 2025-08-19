import asyncio
import logging

from aiogram import Bot, dispatcher, F, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from pyexpat.errors import messages

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message (CommandStart())
async def cmd_start(message: Message):
    await message. answer('Asallomu aleykum\nBotga xush kelibsz ')

@dp.message(Command('xolmurod qanday'))#/xolmurodqanday
async def cmd_salom(messagge: Message):
    await messagge.reply('Xolmurod yaxshi oziz qandaysz ?')

@dp.message(Command('isming'))#/xolmurodqanday
async def cmd_salom(messagge: Message):
    await messagge.reply('Mening ismim bot')

@dp.message(Command('seni kim yaratgan?'))#/xolmurodqanday
async def cmd_salom(messagge: Message):
    await messagge.reply('Meni KENJAYEV XOLMUROD YARATGAN ')

@dp.message(Command('qalesan'))#/xolmurodqanday
async def cmd_salom(messagge: Message):
    await messagge.reply(' yaxshi oziz qandaysz ?')

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Salomlashish", callback_data="salom")],
        [InlineKeyboardButton(text="!Xolmurod haqida", callback_data="xolmurod")],
        [InlineKeyboardButton(text=" ?Yordam", callback_data="yordam")]
    ])
    await message.answer("Assalomu alaykum!\nKerakli bo‘limni tanlang ", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())