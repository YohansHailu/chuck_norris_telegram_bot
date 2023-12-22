import asyncio
import logging


from Bot.bot_instance import bot
from Bot.Handler.message_handler import message_route

from aiogram import Dispatcher


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(message_route)


async def main() -> None:
    dp = Dispatcher()
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
