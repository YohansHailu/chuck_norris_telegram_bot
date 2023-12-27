import asyncio
import logging
import os
from dotenv import load_dotenv
from Bot.bot_instance import bot
from MiddleWares.UserInfo import UserInfo
from aiogram import Dispatcher
from Persistence.DbContext import user_repo
from Bot.bot_instance import dp
from Handler.message_handler import command_handler

load_dotenv()

async def main() -> None:
    dp.message.middleware(UserInfo(user_repo))
    dp.include_router(command_handler)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
