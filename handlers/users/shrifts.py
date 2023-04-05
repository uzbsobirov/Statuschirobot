from keyboards.inline.shrifts import shrifts
from loader import dp, bot, db

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🖌️ Matn shrifti", state='*')
async def shrift_of_text(message: types.Message, state: FSMContext):
    with open(file='media/shrifts.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption="<b>🖌️ Matn shriftini tanlang👇</b>", reply_markup=shrifts)