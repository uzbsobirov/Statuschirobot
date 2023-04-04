from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📝 Rasmga Status Tayorlash ✍️"
            )
        ],
        [
            KeyboardButton(
                text="⚙️ Sozlamalar"
            ),
            KeyboardButton(
                text="📋 Qoʻllanma"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)