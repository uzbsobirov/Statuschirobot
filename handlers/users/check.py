from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.default.main import main, main_admin
from loader import dp, db, bot
from utils.misc.subscription import check
from data.config import ADMINS
@dp.callback_query_handler(text="check_subs", state='*')
async def check_func(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    full_name = call.from_user.id

    await call.answer("Obuna tekshirilmoqda...")
    final_status = True

    result = InlineKeyboardMarkup(row_width=1)

    lst_channels = await db.select_row_panel()
    # rows = await db.select_row_panel()
    if len(lst_channels) >= 1:
        for channel in lst_channels:
            status = await check(user_id=call.from_user.id, channel=channel[1])
            channel = await bot.get_chat(channel[1])
            invite_link = await channel.export_invite_link()
            if status is not True:
                final_status *= False
                result.insert(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
        result.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

        if final_status:
            await call.message.delete()
            if user_id == int(ADMINS[0]):
                await call.message.answer(text=f"<b>Assalomu alaykum "
                                               f"{full_name}\n\n✔️ "
                                               f"Boshlash uchun "
                                               f"tugmalardan birini tanlang...</b>",
                                          reply_markup=main_admin)
            else:
                await call.message.answer(text=f"<b>Assalomu alaykum "
                                               f"{full_name}\n\n✔️ "
                                               f"Boshlash uchun "
                                               f"tugmalardan birini tanlang...</b>",
                                          reply_markup=main)
            await state.finish()
        else:
            await call.message.delete()
            await call.message.answer(text="<b>❌Siz ba'zi kanallardan chiqib ketgansiz, agar kanallarga "
                                           "ulanmasangiz botni ishlata olmaysiz</b>", reply_markup=result,
                                      disable_web_page_preview=True)
            await state.finish()
    else:
        await call.message.delete()
        if user_id == int(ADMINS[0]):
            await call.message.answer(text=f"<b>Assalomu alaykum "
                                           f"{full_name}\n\n✔️ "
                                           f"Boshlash uchun "
                                           f"tugmalardan birini tanlang...</b>",
                                            reply_markup=main_admin)
        else:
            await call.message.answer(text=f"<b>Assalomu alaykum "
                                                                     f"{full_name}\n\n✔️ "
                                                                     f"Boshlash uchun "
                                                                     f"tugmalardan birini tanlang...</b>",
                                            reply_markup=main)