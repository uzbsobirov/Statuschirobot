from keyboards.default.settings import settings
from keyboards.inline.place import places
from loader import dp, bot, db, db_json
from states.settings import Settings

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🏷️ Matn joylashuvi", state='*')
async def shrift_of_text(message: types.Message, state: FSMContext):
    await Settings.place.set()

    await message.answer(text="<b>Matn joylashuvini tanlang👇</b>", reply_markup=places)

@dp.callback_query_handler(state=Settings.place)
async def state_shrift_setting(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = call.data


    if data == 'top_left':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ↖️</b>")

    elif data == 'top_center':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ⬆️</b>")

    elif data == 'top_right':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ↗️</b>")

    elif data == 'left':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ⬅️</b>")

    elif data == 'center':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ⏺</b>")

    elif data == 'right':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy rangi tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ➡️</b>")

    elif data == 'bottom_left':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy rangi tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ↙️</b>")

    elif data == 'bottom_center':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy rangi tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ⬇️</b>")

    elif data == 'bottom_right':
        await db.update_text_place(text_place=data, user_id=user_id)
        await db_json.update_text_place(text_place=data, user_id=user_id)
        await call.message.edit_text(text="<b>✅Status matnining doimiy rangi tanlandi\n\n"
                                                "🏷️ Matn joylashuvi: ↘️</b>")

    else:
        await call.message.delete()
        """
        Back to Settings menu
        """
        text = "Kerakli bo'limni tanlang 👇"
        await call.message.answer(text=text, reply_markup=settings)

    await Settings.main.set()
