from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def build_servers_keyboard(data):
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    for server in data:
        button = KeyboardButton(server['name'])
        keyboard.add(button)
    return keyboard