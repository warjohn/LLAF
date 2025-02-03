        # -*- coding: utf-8 -*-
import asyncio
import logging
import threading

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware
from aiogram.client.bot import DefaultBotProperties

import config as cfg

from routers.router_start import router_start
from routers.router_about import router_about
from routers.router_buy import router_buy
from routers.router_saler import router_saler
from routers.router_admin import router_admin
from routers.router_hotsales import router_hotsales

async def start_bot():
    bot = Bot(token=cfg.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router_start)
    dp.include_router(router_about)
    dp.include_router(router_buy)
    dp.include_router(router_saler) 
    dp.include_router(router_admin)
    dp.include_router(router_hotsales)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())




if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования
        format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логов
        handlers=[
            logging.FileHandler('bot.log'),  # Запись логов в файл
            logging.StreamHandler()  # Вывод логов в консоль
        ]
    )
    asyncio.run(start_bot())