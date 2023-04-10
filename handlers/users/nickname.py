import requests

from loader import dp
from states.nickname import Nick

from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler(text="🖋 Ismga nik yasash", state='*')
async def make_nickname(message: types.Message, state: FSMContext):
    await message.answer(text="<b>Ismingizni kiriting...</b>")
    await Nick.name.set()

@dp.message_handler(state=Nick.name)
async def nickname(message: types.Message, state: FSMContext):
    name = message.text

    url = f"http://apilar.uz/api/name/index.php?text={name}"
    request = requests.post(url=url).json()
    text = f"<b>{name} ismiga niklar👇\n\n</b>"

    for nick in request:
        text += f"<code>{nick}</code>\n"
    text += "\n\n<b>✅ @statuschirobot orqali taqdim etildi!</b>"
    await message.answer(text=text)
    await state.finish()