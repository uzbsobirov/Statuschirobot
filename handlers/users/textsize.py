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

@dp.callback_query_handler(state=Settings.size)
async def state_shrift_setting(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = call.data


    if data == '25':
        await db.update_text_size(text_size=int(data), user_id=user_id)
        await db_json.update_text_size(text_size=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy hajmi tanlandi\n\n"
                                                "📏 Matn hajmi 25%</b>")

    elif data == '50':
        await db.update_text_size(text_size=int(data), user_id=user_id)
        await db_json.update_text_size(text_size=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy hajmi tanlandi\n\n"
                                                "📏 Matn hajmi 50%</b>")

    elif data == '75':
        await db.update_text_size(text_size=int(data), user_id=user_id)
        await db_json.update_text_size(text_size=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy hajmi tanlandi\n\n"
                                                "📏 Matn hajmi 75%</b>")

    elif data == '100':
        await db.update_text_size(text_size=int(data), user_id=user_id)
        await db_json.update_text_size(text_size=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy hajmi tanlandi\n\n"
                                                "📏 Matn hajmi 100%</b>")


    else:
        await call.message.delete()
        """
        Back to Settings menu
        """
        text = "Kerakli bo'limni tanlang 👇"
        await call.message.answer(text=text, reply_markup=settings)

    await Settings.main.set()
