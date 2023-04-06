import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.main import main
from loader import dp, db, bot, db_json


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            text_size=0,
            text_color='yellow',
            text_place='center',
            text_shrift='shrift1'
        )

        await db_json.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            text_size=0,
            text_color='yellow',
            text_place='center',
            text_shrift='shrift1'
        )

        for admin in ADMINS:
            # About message to ADMIN
            msg = f"{user_mention} [<code>{user_id}</code>] bazaga qo'shildi."
            await bot.send_message(chat_id=admin, text=msg)

    except Exception as error:
        logging.info(error)
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"{user_mention} [<code>{user_id}</code>] bazaga oldin qo'shilgan")

    text = f"<b>Assalomu alaykum {user_mention}\n\n✔️ Boshlash uchun tugmalardan birini tanlang...</b>"
    await message.answer(text, reply_markup=main)
