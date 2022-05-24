from aiogram import types, Dispatcher
from config1 import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Как называеться столица Бразилии?"
    answers = [
        'Мадрид',
        'Бразилиа',
        'Риал',
        'РИМ',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="It is easy",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


# @dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_3)
    question = "Ответы:"
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4'
        '5',
    ]
    photo = open("media/problem1.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )
# @dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("NEXT", callback_data="button_call_4")
    markup.add(button_call_4)
    question = "Ответы:"
    answers = [
        '3',
        '4',
        '1',
        '2',
    ]
    photo = open("media1/qlpython-easy.png", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="It is easy",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )
# @dp.callback_query_handler(lambda call: call.data == "button_call_4")
async def quiz_5(call: types.CallbackQuery):
    question = "Когда придумал питон?"
    answers = [
        '1989',
        '2019',
        '1996',
        '1980',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="It is easy",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4,
                                       lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5,
                                       lambda call: call.data == "button_call_4")