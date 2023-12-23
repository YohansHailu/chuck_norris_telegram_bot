from aiogram import Router
from aiogram.types import  Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import Command
from Bot.Handler.utilites import get_random_compliment, get_random_chuck_norris_jokes, get_random_text_for_here
import requests

message_route = Router()


@message_route.message(Command("start"))
async def start(message: Message):

    await message.reply(f"hello {message.from_user.full_name}")
    await help_message(message)


@message_route.message(Command("help"))
async def help_message(message: Message):
    help_text = (
        "Welcome to the Help section!\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/joke - will tell you a random joke\n"
        "/flirt - it will flirt with you, be careful\n"
        "/chuck - will tell you chuck norris joke\n"
        "/dice- will tell you a random dice role\n"
        "/text_here - will tell you a random text for here\n"
        "* for a normal text it will return the echo of the message"
    )

    await message.reply(help_text, parse_mode=ParseMode.HTML)


@message_route.message(Command("dice"))
async def roll_dice(message: Message):
    import random
    dice_result = random.randint(1, 6)
    await message.reply(f"🎲 You rolled a {dice_result}!")


@message_route.message(Command("joke"))
async def tell_joke(message: Message):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke_data = response.json()
    joke = f"{joke_data['setup']}\n{joke_data['punchline']}"
    await message.reply(joke)


@message_route.message(Command("flirt"))
async def flirt(message: Message):
    await message.reply(get_random_compliment())


@message_route.message(Command("text_here"))
async def text_for_here(message: Message):
    await message.reply(get_random_text_for_here())


@message_route.message(Command("chuck"))
async def tell_chuck(message: Message):
    await message.reply(get_random_chuck_norris_jokes())


@message_route.message()
async def echo(message: Message):
    await message.answer(message.text)
