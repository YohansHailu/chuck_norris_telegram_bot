from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
from aiogram import Dispatcher
import os


load_dotenv()
token = os.getenv('API_KEY')
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher()
