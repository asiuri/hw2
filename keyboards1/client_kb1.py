from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1= KeyboardButton("/start")
b2= KeyboardButton("/quiz")
b3= KeyboardButton("/Timetable")
b4=KeyboardButton("/mem")


kb_client= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,)

kb_client.add(b1).row(b2,b3).insert(b4)


