import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext

from configs.json_works import write_json
from core.bot import bot
from keyboards.yes_or_no import yes_or_no_keyboard
from keyboards.default import default_keyboard
from states.add_vds import AddVDS

logger = logging.getLogger(__name__)

async def add_vds(message: types.Message, state: FSMContext):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')

    await message.answer('Введите имя сервера:')
    await state.set_state(AddVDS.name)

async def add_vds_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Хорошо. Теперь, введите IP-адрес сервера:')
    await state.set_state(AddVDS.ip)

async def add_vds_ip(message: types.Message, state: FSMContext):
    ip = message.text
    await state.update_data(ip=ip)
    await message.answer('Теперь, введите порт сервера:')
    await state.set_state(AddVDS.port)

async def add_vds_port(message: types.Message, state: FSMContext):
    port = message.text
    await state.update_data(port=port)
    await message.answer('Теперь, введите имя пользователь вашего сервера:')
    await state.set_state(AddVDS.username)

async def add_vds_user(message: types.Message, state: FSMContext):
    username = message.text
    await state.update_data(username=username)
    await message.answer('Теперь, введите пароль пользователя вашего сервера:')
    await state.set_state(AddVDS.password)

async def add_vds_password(message: types.Message, state: FSMContext):
    password = message.text
    await state.update_data(password=password)
    data = await state.get_data()
    name = data.get('name')
    ip = data.get('ip')
    port = data.get('port')
    username = data.get('username')
    password = data.get('password')
    await bot.send_message(message.chat.id,
        md.text(
            'Проверьте правильность введенных данных:',
            md.bold('Имя сервера: ') + md.escape_md(name),
            md.bold('IP: ') + md.escape_md(ip),
            md.bold('Порт: ') + md.escape_md(port),
            md.bold('Пользователь: ') + md.escape_md(username),
            md.bold('Пароль: ') + md.escape_md(password),
            sep = '\n'
        ), parse_mode='MarkdownV2')
    await message.answer('Если все данные верны, нажмите кнопку "✅ Подтвердить", если нет, нажмите кнопку "❌ Отменить"', reply_markup=yes_or_no_keyboard)
    await state.set_state(AddVDS.confirm)

async def add_vds_confirm(message: types.Message, state: FSMContext):
    if message.text == '✅ Подтвердить':
        data = await state.get_data()
        name = data.get('name')
        ip = data.get('ip')
        port = data.get('port')
        username = data.get('username')
        password = data.get('password')
        await write_json({
            'name': name,
            'ip': ip,
            'port': port,
            'username': username,
            'password': password
        })
        await message.answer('✅ Сервер успешно добавлен', reply_markup=default_keyboard)
        await state.finish()
    elif message.text == '❌ Отменить':
        await message.answer('❌ Вы отменили добавление сервера', reply_markup=default_keyboard)
        await state.finish()


def setup(dp: Dispatcher):
    dp.register_message_handler(add_vds, Text(equals = '💻 Добавить сервер'), state='*')
    dp.register_message_handler(add_vds, commands=['add_vds'], state='*')
    dp.register_message_handler(add_vds_name, state=AddVDS.name)
    dp.register_message_handler(add_vds_ip, state=AddVDS.ip)
    dp.register_message_handler(add_vds_port, state=AddVDS.port)
    dp.register_message_handler(add_vds_user, state=AddVDS.username)
    dp.register_message_handler(add_vds_password, state=AddVDS.password)
    dp.register_message_handler(add_vds_confirm, Text(equals = ['✅ Подтвердить', '❌ Отменить']), state=AddVDS.confirm)
