import asyncio
from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.admin import admin



@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.message_handler(text="💻 Admin panel", state='*', user_id=ADMINS)
async def get_all_users(message: types.Message):

    full_name = message.from_user.full_name
    await message.answer(f"{full_name} Admin panelga xush kelibsiz👣", reply_markup=admin)

