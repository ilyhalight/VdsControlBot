from configs.load import load_cfg
from core.bot import bot

settings = load_cfg()['main']


async def on_startup(dp):
    await bot.send_message(settings['chat_id'], '✅ Бот был запущен')

async def on_shutdown(dp):
    await bot.send_message(settings['chat_id'], '❗ Бот был выключен')