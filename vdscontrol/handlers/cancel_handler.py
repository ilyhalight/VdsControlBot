import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from core.bot import bot
from keyboards.default import default_keyboard


async def cancel(message: types.Message, state: FSMContext):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')
    await state.finish()
    await bot.send_message(message.chat.id, '❌ Действие отменено', reply_markup = default_keyboard)

def setup(dp: Dispatcher):
    dp.register_message_handler(cancel, commands = ['cancel'])
    dp.register_message_handler(cancel, Text(equals = ['❌ Отменить', '❌ Отмена', 'Отменить', 'Отмена', 'cancel']))