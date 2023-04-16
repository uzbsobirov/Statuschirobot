import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ADMINS
from keyboards.default.main import main, main_admin
from loader import dp, db, bot, db_json
from utils.misc.subscription import check


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
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
            text_size=50,
            text_color='yellow',
            text_place='center',
            text_shrift='shrift1'
        )

        await db_json.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            text_size=50,
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

    lst_channels = await db.select_row_panel()
    if len(lst_channels) >= 1:
        # We check if user is not subs to channel
        for row in lst_channels:
            status = await check(user_id=message.from_user.id, channel=row[1])
        if status == False:
            markup = InlineKeyboardMarkup(row_width=1)
            for channel in lst_channels:
                chat = await bot.get_chat(channel[1])
                invite_link = await chat.export_invite_link()
                markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
            markup.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

            text = f"<b>Assalomu aleykum</b>, {full_name}! Botdan to'liq foydalanish uchun homiy kanallarimizga a'zo " \
                   f"bo'ling"
            await message.answer(text=text, reply_markup=markup, disable_web_page_preview=True)
            await state.finish()
        else:
            text = f"<b>Assalomu alaykum {user_mention}\n\n✔️ Boshlash uchun tugmalardan birini tanlang...</b>"
            if user_id == int(ADMINS[0]):
                await message.answer(text, reply_markup=main_admin)
            else:
                await message.answer(text, reply_markup=main)
    else:
        text = f"<b>Assalomu alaykum {user_mention}\n\n✔️ Boshlash uchun tugmalardan birini tanlang...</b>"
        if user_id == int(ADMINS[0]):
            await message.answer(text, reply_markup=main_admin)
        else:
            await message.answer(text, reply_markup=main)
