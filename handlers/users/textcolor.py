from keyboards.default.settings import settings
from keyboards.inline.color import colors
from loader import dp, bot, db, db_json
from states.settings import Settings

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🔖 Matn rangi", state='*')
async def shrift_of_text(message: types.Message, state: FSMContext):
    await Settings.color.set()

    await message.answer(text="<b>🖌️ Matn hajmini tanlang👇</b>", reply_markup=colors)

@dp.callback_query_handler(state=Settings.color)
async def state_shrift_setting(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = call.data


    if data == 'white':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🔖 Matn rangi: <i>⚪️ Oq</i></b>")

    elif data == 'black':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🔖 Matn rangi: <i>⚫️ Qora</i></b>")

    elif data == 'yellow':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🔖 Matn rangi: <i>🟡 Sariq</i></b>")

    elif data == 'green':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🔖 Matn rangi: <i>🟢 Yashil</i></b>")

    elif data == 'blue':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🔖 Matn rangi: <i>🔵 Ko'k</i></b>")

    elif data == 'purple':
        await db.update_text_color(text_color=data, user_id=user_id)
        await db_json.update_text_color(text_color=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy rangi tanlandi\n\n"
                                                "🔖 Matn rangi: <i>🟣 Pushti</i></b>")

    else:
        await call.message.delete()
        """
        Back to Settings menu
        """
        text = "Kerakli bo'limni tanlang 👇"
        await call.message.answer(text=text, reply_markup=settings)

    await Settings.main.set()
