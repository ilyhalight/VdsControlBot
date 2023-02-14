from aiogram.dispatcher.filters.state import State, StatesGroup


class AddVDS(StatesGroup):
    name = State()
    ip = State()
    port = State()
    username = State()
    password = State()
    confirm = State()
