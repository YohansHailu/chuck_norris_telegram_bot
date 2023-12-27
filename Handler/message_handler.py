from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import Command
from Keyboards.LikeItKb import get_inline_markup

from Bot.bot_instance import dp

import requests
from Handler import utility

command_handler = Router()

@command_handler.message(Command("start"))
async def start(message: Message):
    await message.reply(f"hello {message.from_user.full_name}")
    await help_message(message)




@command_handler.message(Command("help"))
async def help_message(message: Message):
    help_text = (
        "Welcome to the Help section!\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/coding_joke - will tell you a random joke\n"
        "/text_her - will tell you a random text for her\n"
        "/chuck - will tell you chuck norris joke\n"
        "/dice- will tell you a random dice role\n"
    )

    await message.reply(help_text, parse_mode=ParseMode.HTML)



async def reply(message: Message, obj):
    print(obj)
    text = obj['text']
    await message.reply(text, reply_markup=get_inline_markup(obj))

@command_handler.message(Command("text_her"))
async def text_for_her(message: Message):
    obj = utility.text_for_her()
    await reply(message, obj)


@command_handler.message(Command("chuck"))
async def tell_chuck(message: Message):
    obj = utility.tell_chuck()
    await reply(message, obj)

@command_handler.message(Command("coding_joke"))
async def tell_coding_joke(message: Message):
    obj = utility.tell_coding_joke()
    await reply(message, obj)

@command_handler.message()
async def echo(message: Message):
    await message.answer("only send commands!")

@command_handler.message(Command("dice"))
async def roll_dice(message: Message):
    import random
    dice_result = random.randint(1, 6)
    await message.reply(f"🎲 You rolled a {dice_result}!")
