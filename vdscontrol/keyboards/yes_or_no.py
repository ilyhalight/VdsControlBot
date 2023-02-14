from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_or_no_phrases = ['✅ Подтвердить', '❌ Отменить']

yes_or_no_keyboard = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)

button1 = KeyboardButton(yes_or_no_phrases[0])
button2 = KeyboardButton(yes_or_no_phrases[1])

yes_or_no_keyboard.add(button1, button2)