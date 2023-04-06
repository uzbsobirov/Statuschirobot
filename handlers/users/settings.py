from keyboards.default.settings import settings
from loader import dp, bot, db

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.settings import Settings


@dp.message_handler(text="⚙️ Sozlamalar", state='*')
async def setting_handler(message: types.Message, state: FSMContext):
    text = "<b>Kerakli bo'limni tanlang 👇</b>"
    await message.answer(text=text, reply_markup=settings)
    await Settings.main.set()