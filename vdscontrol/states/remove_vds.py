from aiogram.dispatcher.filters.state import State, StatesGroup


class RemoveVDS(StatesGroup):
    name = State()
    confirm = State()