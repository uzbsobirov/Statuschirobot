from aiogram.dispatcher.filters.state import StatesGroup, State

class Settings(StatesGroup):
    main = State()
    shrifts = State()
    size = State()
    color = State()
    place = State()