from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sizes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="🏷️25%", callback_data='25'
                ),
            InlineKeyboardButton(
                    text="🏷️50%", callback_data='50'
                )
        ],
        [
            InlineKeyboardButton(
                    text="🏷️75%", callback_data='75'
                ),
            InlineKeyboardButton(
                    text="🏷️100%", callback_data='100'
                ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Orqaga", callback_data='size_back_to_settings'
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)