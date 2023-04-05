from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🏷️ Matn joylashuvi"
            ),
            KeyboardButton(
                text="📏 Matn hajmi"
            )
        ],
        [
            KeyboardButton(
                text="🖌️ Matn shrifti"
            ),
            KeyboardButton(
                text="🔖 Matn rangi"
            )
        ],
        [
            KeyboardButton(
                text="⚙️ Mening sozlamalarim"
            )
        ],
        [
            KeyboardButton(
                text="⬅️ Orqaga"
            )
        ]

    ], resize_keyboard=True, one_time_keyboard=True
)