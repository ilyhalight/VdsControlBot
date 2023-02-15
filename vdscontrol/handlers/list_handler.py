import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md

from configs.json_works import read_json
from core.bot import bot
from keyboards.default import default_keyboard

logger = logging.getLogger(__name__)

async def list(message: types.Message):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')

    try:
        data = await read_json()
    except Exception as err:
        logger.exception(err)
        data = None

    servers = '\n'.join((f'{server["name"]} - {server["ip"]}' for server in data)) if data else 'Список пуст'

    await bot.send_message(message.chat.id,
    md.text(
        md.bold(f'Список добавленных серверов ({len(data)}):'),
        md.code(servers),
        sep = '\n'
    ), parse_mode='MarkdownV2', reply_markup=default_keyboard)

def setup(dp: Dispatcher):
    dp.register_message_handler(list, Text(equals = '📝 Список серверов'))
    dp.register_message_handler(list, commands=['list'])
