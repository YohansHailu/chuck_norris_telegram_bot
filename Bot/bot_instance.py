from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('API_KEY')

##session=AiohttpSession(proxy='http://proxy.server:3128')
bot = Bot(token=token, parse_mode="HTML")
