import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs.load import load_cfg

settings = load_cfg()['main']


bot = Bot(token = os.environ.get('BOT_TOKEN'))
bot._settings = settings
dp = Dispatcher(bot, storage=MemoryStorage())