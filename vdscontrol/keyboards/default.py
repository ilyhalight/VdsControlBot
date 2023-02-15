from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

default_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)

button1 = KeyboardButton('📰 Информация')
button2 = KeyboardButton('📝 Список серверов')
button3 = KeyboardButton('💻 Добавить сервер')
button4 = KeyboardButton('🗑 Удалить сервер')

default_keyboard.add(button1, button2, button3, button4)