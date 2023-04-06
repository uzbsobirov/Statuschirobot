from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

colors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="⚪️ Oq", callback_data='white'
                ),
            InlineKeyboardButton(
                    text="⚫️ Qora", callback_data='black'
                )
        ],
        [
            InlineKeyboardButton(
                    text="🟡 Sariq", callback_data='yellow'
                ),
            InlineKeyboardButton(
                    text="🟢 Yashil", callback_data='green'
                ),
        ],
        [
            InlineKeyboardButton(
                    text="🔵 Ko'k", callback_data='blue'
                ),
            InlineKeyboardButton(
                    text="🟣 Pushti", callback_data='purple'
                ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Orqaga", callback_data='color_back_to_settings'
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)