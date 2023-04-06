from loader import dp
from states.settings import Settings
from keyboards.default.main import main
from keyboards.default.settings import settings

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="⬅️ Orqaga", state=Settings.main)
async def back_to_main(message: types.Message, state: FSMContext):
    """
    Back to Main menu
    """
    text = f"<b>Asosiy menu</b>"
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