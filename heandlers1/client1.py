from aiogram import types, Dispatcher
from config1 import bot, dp
from keyboards1 import kb_client
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import random


#@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id,'What can i do for you',reply_markup=kb_client)
        await message.delete()
    except:
        await message .reply('You can talk to her only privet,here is her:\n@Uri18bot')


#@dp.message_handler(commands=['Timetable'])
async def time_table (message:types.Message):
     await bot.send_message(message.from_user.id,
          'Monday-Friday from 9:00 till 17:00 oclock,Sat-Sun are weekend')



#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types .Message):
    markup=InlineKeyboardMarkup()
    button_call_1=InlineKeyboardButton("NEXT",callback_data="button_call_1")
    markup.add(button_call_1)
    question="Как вы пишите коментарий в питон?"
    answers=[
          '!',
          '=',
          '#',
          '_'

    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

#@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media1/smeh-9.png", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)
    await message.reply(f"Подождите {message.from_user.full_name}  .Она занята!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(time_table, commands=['timetable'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])







