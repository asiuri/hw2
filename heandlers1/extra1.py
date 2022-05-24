from aiogram import types, Dispatcher
from config1 import bot, dp
import random



# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith("Pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == "game":
        games = random.choice(["🎲", "⚽️", "🏀", "🎯", "🎳", "🎰"])
        await bot.send_dice(message.chat.id, emoji=value)

def register_hendler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
  
