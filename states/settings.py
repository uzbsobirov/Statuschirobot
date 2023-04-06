from aiogram.dispatcher.filters.state import StatesGroup, State

class Settings(StatesGroup):
    main = State()
    shrifts = State()