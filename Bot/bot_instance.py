from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('API_KEY')

bot = Bot(token=token, parse_mode="HTML")
