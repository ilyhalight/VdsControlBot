import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext

from configs.json_works import remove_json
from core.bot import bot
from keyboards.yes_or_no import yes_or_no_keyboard, yes_or_no_phrases
from keyboards.default import default_keyboard
from states.remove_vds import RemoveVDS

logger = logging.getLogger(__name__)

async def remove_vds(message: types.Message, state: FSMContext):
    if message.from_user.id != bot._settings['chat_id']:
        return await message.answer('❌ У вас нет доступа к этой команде')

    await message.answer('Введите имя сервера, который хотите удалить.')
    await state.set_state(RemoveVDS.name)

async def remove_vds_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Вы уверены, что хотите удалить сервер ' + md.code(name) + '?', parse_mode='MarkdownV2', reply_markup=yes_or_no_keyboard)
    await state.set_state(RemoveVDS.confirm)

async def remove_vds_confirm(message: types.Message, state: FSMContext):
    if message.text == yes_or_no_phrases[0]:
        data = await state.get_data()
        name = data.get('name')
        await remove_json(name)
        await message.answer('✅ Сервер успешно удален', reply_markup=default_keyboard)
        await state.finish()
    elif message.text == yes_or_no_phrases[1]:
        await message.answer('❌ Вы отменили удаление сервера', reply_markup=default_keyboard)
        await state.finish()

async def remove_vds_confirm_error(message: types.Message, state: FSMContext):
    await message.answer('❌ Неизвестное действие. Пожалуйста, выберите одно из доступных действий.', reply_markup=yes_or_no_keyboard)


def setup(dp: Dispatcher):
    dp.register_message_handler(remove_vds, Text(equals = '🗑 Удалить сервер'), state='*')
    dp.register_message_handler(remove_vds, commands=['remove_vds'], state='*')
    dp.register_message_handler(remove_vds_name, state=RemoveVDS.name)
    dp.register_message_handler(remove_vds_confirm, Text(equals = yes_or_no_phrases), state=RemoveVDS.confirm)
    dp.register_message_handler(remove_vds_confirm_error,  state=RemoveVDS.confirm)
