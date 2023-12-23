from aiogram import BaseMiddleware
from aiogram.types import Message
from Bot.bot_instance import bot
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


class UserInfo(BaseMiddleware):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def __call__( self, handler, message: Message, data):
        try:
            await self.save_user_info(message)
        except Exception as e:
            print("database Error", e)

        return await handler(message, data)

    async def save_user_info(self, message: Message):
        user = self.user_repo.get_by_chat_id(message.from_user.id)
        if user is None:
            user = {
                "chat_id": message.from_user.id,
                "username": message.from_user.username,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
                "is_bot": message.from_user.is_bot,
                "language_code": message.from_user.language_code,
            }
            self.user_repo.add(user)
            await self.notify_new_user_admin(message)
            log_message = f"new user: {message.from_user.username}"
            logger.info(log_message)
            
        log_message = f"user saved to database"
        logger.info(log_message)
    
    async def notify_new_user_admin(self, message: Message):
        admin_chat_id = os.getenv("ADMIN_CHAT_ID")
        await bot.send_message(admin_chat_id, f"new user: {message.from_user.username}")
        log_message = f"new user notified to admin"
        logger.info(log_message)


