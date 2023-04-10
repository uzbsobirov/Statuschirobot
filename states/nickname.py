from aiogram.dispatcher.filters.state import StatesGroup, State

class Nick(StatesGroup):
    name = State()
