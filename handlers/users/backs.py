from data.config import ADMINS
from loader import dp
from states.settings import Settings
from keyboards.default.main import main, main_admin

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.admin import admin
from keyboards.inline.adv import types_private
from states.admin import *


@dp.message_handler(text="⬅️ Orqaga", state=Settings.main)
async def back_to_main(message: types.Message, state: FSMContext):
    """
    Back to Main menu
    """
    user_id = message.from_user.id
    text = f"<b>Asosiy menu</b>"

    if user_id == ADMINS[0]:
        await message.answer(text, reply_markup=main_admin)
    else:
        await message.answer(text, reply_markup=main)

    await state.finish()


# @dp.callback_query_handler(text="back_to_settings", state='*')
# async def back_toSettings(call: types.CallbackQuery, state: FSMContext):
#     """
#     Back to Settings menu
#     """
#     text = "Kerakli bo'limni tanlang 👇"
#     await call.message.answer(text=text, reply_markup=settings)
#     await state.finish()





# @dp.callback_query_handler(text='back', state='*')
# async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     nphotourl = "https://t.me/forchrabot/30"
#     await call.message.answer_photo(photo=nphotourl, caption="Sizga kerakli bo'lganini tanlang👇", reply_markup=fornamoz)
#     await state.finish()

@dp.callback_query_handler(text='back', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.from_user.id == int(ADMINS[0]):
        await call.message.answer(text="Sizga kerakli bo'lganini tanlang👇", reply_markup=main_admin)
    else:
        await call.message.answer(text="Sizga kerakli bo'lganini tanlang👇", reply_markup=main)
    await state.finish()


@dp.callback_query_handler(text='tomain', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Sizga kerakli bo'lganini tanlang👇", reply_markup=main_admin)
    await state.finish()

@dp.callback_query_handler(text='topanel', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Admin panel", reply_markup=admin)
    await state.finish()

@dp.callback_query_handler(text='topanell', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Admin panel", reply_markup=admin)
    await state.finish()


@dp.callback_query_handler(text="stat_back", state=Admin.stat)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()



# Bu handler xabar yuborish bolimidan Admin panel menuga qaytish uchun
@dp.callback_query_handler(text="stat_back", state=Admin.sending)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()




# @dp.callback_query_handler(text="stat_back", state=SendingUser.user)
# async def back_to_main(call: types.CallbackQuery, state: FSMContext):
#     user_id = call.from_user.id
#
#     text = "<b>Keraklisini tanlang👇</b>"
#     await call.message.edit_text(text=text, reply_markup=type_sending)
#     await Admin.sending.set()
#

@dp.callback_query_handler(text="bad_words_back_back", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()

@dp.callback_query_handler(text="back_private_adv", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_private)
    await SendingUser.user.set()


@dp.callback_query_handler(text="to_admin_main", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panel</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await state.finish()

