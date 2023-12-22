from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from Bot.Handler.utilites import get_random_compliment, get_random_chuck_norris_jokes
import requests

message_route = Router()


@message_route.message(Command("start"))
async def start(message: types.Message):
    await message.reply(f"hello {message.from_user.full_name}")
    await help_message(message)


@message_route.message(Command("help"))
async def help_message(message: types.Message):
    help_text = (
        "Welcome to the Help section!\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/joke - will tell you a random joke\n"
        "/flirt - it will flirt with you, be careful\n"
        "/chuck - will tell you chuck norris joke\n"
        "/dice- will tell you a random dice role\n"

        "* for a normal text it will return the echo of the message"
    )

    await message.reply(help_text, parse_mode=ParseMode.HTML)


@message_route.message(Command("dice"))
async def roll_dice(message: types.Message):
    import random
    dice_result = random.randint(1, 6)
    await message.reply(f"🎲 You rolled a {dice_result}!")


@message_route.message(Command("joke"))
async def tell_joke(message: types.Message):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke_data = response.json()
    joke = f"{joke_data['setup']}\n{joke_data['punchline']}"
    await message.reply(joke)


@message_route.message(Command("flirt"))
async def flirt(message: types.Message):
    await message.reply(get_random_compliment())


@message_route.message(Command("chuck"))
async def tell_chuck(message: types.Message):
    await message.reply(get_random_chuck_norris_jokes())


@message_route.message()
async def echo(message: types.Message):
    await message.answer(message.text)
