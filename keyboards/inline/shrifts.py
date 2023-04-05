from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

shrifts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="🖌️ 1", callback_data='shrift1'
                ),
            InlineKeyboardButton(
                    text="🖌️ 2", callback_data='shrift2'
                ),
            InlineKeyboardButton(
                    text="🖌️ 3", callback_data='shrift3'
                )
        ],
        [
            InlineKeyboardButton(
                    text="🖌️ 4", callback_data='shrift4'
                ),
            InlineKeyboardButton(
                    text="🖌️ 5", callback_data='shrift5'
                ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Orqaga", callback_data='back_to_settings'
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)