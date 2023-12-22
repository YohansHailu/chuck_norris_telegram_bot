from aiogram import Bot
import os

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('API_KEY') or "NO API TOKEN"

bot = Bot(token=token, parse_mode="HTML")