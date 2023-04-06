from keyboards.inline.shrifts import shrifts
from keyboards.default.settings import settings
from loader import dp, bot, db, db_json
from states.settings import Settings

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🖌️ Matn shrifti", state='*')
async def shrift_of_text(message: types.Message, state: FSMContext):
    await Settings.shrifts.set()

    with open(file='media/shrifts.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption="<b>🖌️ Matn shriftini tanlang👇</b>", reply_markup=shrifts)


@dp.callback_query_handler(state=Settings.shrifts)
async def state_shrift_setting(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = call.data


    if data == 'shrift1':
        await db.update_text_shrift(text_shrift=data, user_id=user_id)
        await db_json.update_text_shrift(text_shrift=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🖌️ Siz 1-shriftni tanladingiz</b>")
    elif data == 'shrift2':
        await db.update_text_shrift(text_shrift=data, user_id=user_id)
        await db_json.update_text_shrift(text_shrift=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🖌️ Siz 2-shriftni tanladingiz</b>")
    elif data == 'shrift3':
        await db.update_text_shrift(text_shrift=data, user_id=user_id)
        await db_json.update_text_shrift(text_shrift=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🖌️ Siz 3-shriftni tanladingiz</b>")
    elif data == 'shrift4':
        await db.update_text_shrift(text_shrift=data, user_id=user_id)
        await db_json.update_text_shrift(text_shrift=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🖌️ Siz 4-shriftni tanladingiz</b>")
    elif data == 'shrift5':
        await db.update_text_shrift(text_shrift=data, user_id=user_id)
        await db_json.update_text_shrift(text_shrift=data, user_id=user_id)
        await call.message.edit_caption(caption="<b>✅Status matnining doimiy shrifti tanlandi\n\n"
                                                "🖌️ Siz 5-shriftni tanladingiz</b>")
    else:
        await call.message.delete()
        """
        Back to Settings menu
        """
        text = "Kerakli bo'limni tanlang 👇"
        await call.message.answer(text=text, reply_markup=settings)
        await state.finish()



