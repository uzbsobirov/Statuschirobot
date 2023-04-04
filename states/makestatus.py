from aiogram.dispatcher.filters.state import StatesGroup, State

class Status(StatesGroup):
    image = State()
    text = State()