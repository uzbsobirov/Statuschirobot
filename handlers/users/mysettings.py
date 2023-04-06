from loader import dp, db
from .detectors import detect_color, detect_size

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="⚙️ Mening sozlamalarim", state='*')
async def my_setting(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    user_datas = await db.select_one_user(user_id=user_id)
    place = user_datas[0][4]
    shrift = user_datas[0][5]
    size = user_datas[0][6]
    color = user_datas[0][7]



    text = f"⚙️ Sizning sozlamalaringiz👇\n\n🏷️ Matn joylashuvi: {place}\n" \
           f"🖌️ Matn shrifti: {shrift}\n📏 Matn hajmi: {detect_size(size=size)}\n🔖 Matn rangi: {detect_color(color=color)}"

    await message.answer(text=text)