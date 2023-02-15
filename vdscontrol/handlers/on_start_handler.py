import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from core.bot import bot
from keyboards.default import default_keyboard


async def on_start(message: types.Message, state: FSMContext):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')
    await state.finish()
    await bot.send_message(message.chat.id, md.text(f'👋 Привет, {md.bold(message.from_user.full_name)}! Я бот, который поможет тебе управлять VDS.'), parse_mode=types.ParseMode.MARKDOWN, reply_markup = default_keyboard)

def setup(dp: Dispatcher):
    dp.register_message_handler(on_start, commands = ['start'])