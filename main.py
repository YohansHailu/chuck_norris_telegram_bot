import asyncio
import logging
import os
from dotenv import load_dotenv
from Bot.bot_instance import bot
from Bot.Handler.message_handler import message_route
from MiddleWares.UserInfo import UserInfo
from aiogram import Dispatcher
from Persistence.Respository import Repository
load_dotenv()


def register_user_info_middlewares() -> None:

    MONGODB_URL = os.getenv("MONGODB_URL")
    DB_NAME = os.getenv("DB_NAME")
    USER_COLLECTION_NAME = os.getenv("USER_COLLECTION_NAME")
    
    try:
        user_repo = Repository(MONGODB_URL, DB_NAME, USER_COLLECTION_NAME)
        message_route.message.middleware(UserInfo(user_repo))
    except Exception as e:
        print("database Error", e)


def register_handlers(dp: Dispatcher) -> None:

    dp.include_router(message_route)

async def main() -> None:
    dp = Dispatcher()
    
    register_handlers(dp)
    register_user_info_middlewares()

    await dp.start_polling(bot)

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
