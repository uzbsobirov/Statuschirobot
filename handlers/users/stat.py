from loader import dp, db, db_json
from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import date
from keyboards.inline.admin import back


@dp.callback_query_handler(text="statistika", state='*')
async def statis(call: types.CallbackQuery, state: FSMContext):
    stat = await db.count_users()
    statjson = await db_json.select_all_users()
    today = date.today()

    if len(statjson) >= stat:
        text = f"<b>📆 Bugunki sana: {today}\n\n📊 Bot obunachilari: {len(statjson)}\n\n⚡️@islamiuzbot</b>"
        await call.message.edit_text(text=text, reply_markup=back)
    else:
        text = f"<b>📆 Bugunki sana: {today}\n\n📊 Bot obunachilari: {stat}\n\n⚡️@islamiuzbot</b>"
        await call.message.edit_text(text=text, reply_markup=back)
    await state.finish()