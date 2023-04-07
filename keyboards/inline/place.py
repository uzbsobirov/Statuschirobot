from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

places = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="ㅤ", callback_data='top_left'
                ),
            InlineKeyboardButton(
                    text="⬆️", callback_data='top_center'
                ),
            InlineKeyboardButton(
                    text="ㅤ", callback_data='top_right'
                )
        ],
        [
            InlineKeyboardButton(
                    text="⬅️", callback_data='left'
                ),
            InlineKeyboardButton(
                    text="⏺", callback_data='center'
                ),
            InlineKeyboardButton(
                    text="➡️", callback_data='right'
                )
        ],
        [
            InlineKeyboardButton(
                    text="ㅤ", callback_data='bottom_left'
                ),
            InlineKeyboardButton(
                    text="⬇️", callback_data='bottom_center'
                ),
            InlineKeyboardButton(
                    text="ㅤ", callback_data='bottom_right'
                )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Orqaga", callback_data='place_back_to_settings'
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)