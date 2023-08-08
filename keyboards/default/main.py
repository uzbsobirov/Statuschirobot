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

main_admin = ReplyKeyboardMarkup(
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
        ],
        [
            KeyboardButton(
                text="💻 Admin panel"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)