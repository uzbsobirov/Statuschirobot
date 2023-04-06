from keyboards.default.settings import settings
from keyboards.inline.size import sizes
from loader import dp, bot, db, db_json
from states.settings import Settings

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="📏 Matn hajmi", state='*')
async def shrift_of_text(message: types.Message, state: FSMContext):
    await Settings.size.set()

    with open(file='media/textsize.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption="<b>🖌️ Matn hajmini tanlang👇</b>", reply_markup=sizes)