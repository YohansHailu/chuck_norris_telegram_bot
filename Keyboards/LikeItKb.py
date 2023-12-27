from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from Bot.bot_instance import bot
from aiogram import Router, types
from aiogram.filters.callback_data import CallbackData


class activity_callback_data(CallbackData, prefix="activity"):
    obj_id:str
    activity:str


def get_inline_markup(obj):

    id = str(obj["_id"])
    like_count = obj.get('like', 0)
    love_count = obj.get('love', 0)
    funny_count = obj.get('funny', 0)

    like_button = InlineKeyboardButton(text=f"👍 {like_count}", callback_data=activity_callback_data(obj_id=id, activity="like").pack())
    love_button = InlineKeyboardButton(text=f"❤️ {love_count}", callback_data=activity_callback_data(obj_id=id, activity="love").pack())
    funny_button = InlineKeyboardButton(text=f"😄 {funny_count}", callback_data=activity_callback_data(obj_id=id, activity="funny").pack())


    reaction_kb = InlineKeyboardMarkup(inline_keyboard=[[like_button, love_button, funny_button]])
    return reaction_kb 




activity_callback_router = Router()

@activity_callback_router.callback_query(lambda x: x.data.startswith("activity"))
async def acivity_callback(callback_query:types.CallbackQuery):
    data=CallbackData.unpack(callback_query.data)
    print(data)
    ##await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=get_inline_markup(obj))
    ##await callback_query.message.answer("you like it don't you ")
