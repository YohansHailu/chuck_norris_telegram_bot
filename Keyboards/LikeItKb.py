from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from Bot.bot_instance import dp


def get_inline_markup(obj):

    like_count = obj.get('like_count', 0)
    love_count = obj.get('love_count', 0)
    funny_count = obj.get('funny_count', 0)

    like_button = InlineKeyboardButton(text=f"👍 {like_count}", callback_data='like_button_pressed')
    love_button = InlineKeyboardButton(text=f"❤️ {love_count}", callback_data='love_button_pressed')
    funny_button = InlineKeyboardButton(text=f"😄 {funny_count}", callback_data='funny_button_pressed')

    reaction_kb = InlineKeyboardMarkup(inline_keyboard=[[like_button, love_button, funny_button]])
    return reaction_kb 


