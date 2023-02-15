import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext

from configs.json_works import read_json
from core.bot import bot
from core.commands import get_info
from keyboards.servers import build_servers_keyboard
from keyboards.default import default_keyboard
from states.stats_vds import StatsVDS

logger = logging.getLogger(__name__)

async def stats(message: types.Message, state: FSMContext):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')

    try:
        data = await read_json()
    except Exception as err:
        logger.exception(err)
        data = None

    if not data:
        return await bot.send_message(message.chat.id, '❌ Не удалось получить информацию о серверах', reply_markup=default_keyboard)
    
    await bot.send_message(message.chat.id, 'Выберите сервер:', reply_markup = build_servers_keyboard(data))
    await state.set_state(StatsVDS.name)

async def get_stats(message: types.Message, state: FSMContext):
    name = message.text

    try:
        data = await read_json()
    except Exception as err:
        logger.exception(err)
        data = None

    if not data:
        await state.finish()
        return await bot.send_message(message.chat.id, '❌ Не удалось получить информацию о серверах', reply_markup=default_keyboard)
    
    server_data = None
    for server in data:
        if name == server['name']:
            server_data = server
            break

    if not server_data:
        await state.finish()
        return await bot.send_message(message.chat.id, '❌ Не удалось получить информацию о сервере', reply_markup=default_keyboard)

    try:
        vds_data = await get_info(server_data['ip'], server_data['username'], server_data['password'], int(server_data['port']))
    except Exception as err:
        logger.exception(err)
        await state.finish()
        return await bot.send_message(message.chat.id, '❌ Не удалось получить информацию о сервере', reply_markup=default_keyboard)
    if not vds_data['status']:
        await state.finish()
        return await bot.send_message(message.chat.id, vds_data['error'], reply_markup=default_keyboard)

    disks = '\n'.join(disk for disk in vds_data['disks'])
    await bot.send_message(message.chat.id,
    md.text(
        md.bold('Информация о сервере:'),
        md.bold('Name: ') + md.escape_md(server_data['name']),
        md.bold('IP: ') + md.escape_md(server_data['ip']),
        md.bold('OS: ') + md.escape_md(vds_data['os']),
        md.bold('Host: ') + md.escape_md(vds_data['host']),
        md.bold('Kernel: ') + md.escape_md(vds_data['kernel']),
        md.bold('Uptime: ') + md.escape_md(vds_data['uptime']),
        md.bold('Packages: ') + md.escape_md(vds_data['packages']),
        md.bold('Shell: ') + md.escape_md(vds_data['shell']),
        md.bold('CPU: ') + md.escape_md(vds_data['cpu']),
        md.bold('Memory: ') + md.escape_md(vds_data['memory']),
        md.bold('Disks: '),
        md.code(disks),
        sep = '\n'
    ), parse_mode='MarkdownV2', reply_markup=default_keyboard)
    await state.finish()

def setup(dp: Dispatcher):
    dp.register_message_handler(stats, Text(equals = '📊 Статистика'))
    dp.register_message_handler(stats, commands=['stats'])
    dp.register_message_handler(get_stats, state=StatsVDS.name)
