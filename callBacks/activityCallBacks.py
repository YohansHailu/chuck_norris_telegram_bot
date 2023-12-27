from aiogram import Router, types

activity_callback_router = Router()

@activity_callback_router.callback_query(lambda c: c.data.startswith("activity"))
async def acivity_callback(callback_query:types.CallbackQuery):
    await callback_query.message.answer("you like it don't you")

