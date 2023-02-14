import logging
from aiogram import executor

from configs.load import load_env
from core.logger import init_logging

logger = logging.getLogger(__name__)
import os


if __name__ == '__main__':
    init_logging()
    if load_env():
        from core.bot import dp
        from handlers.register import register_handlers
        from core.events import on_startup, on_shutdown
        token = os.environ.get('BOT_TOKEN')
        logger.info(token)
        register_handlers(dp)
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    else:
        logger.error('Failed to load environment variables')
        exit(1)