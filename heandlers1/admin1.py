from aiogram import types, Dispatcher
from config1 import bot, ADMIN1
from aiogram import types, Dispatcher
from config import bot, dp

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN1:
            await message.reply("You can not order me!")
        if not message.reply_to_message:
            await message.reply("This Command is only for answer!")
        else:
            await message.bot.kick_chat_member(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id
                                               )
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name} "
                f"You need it!Stop {message.from_user.full_name}"
            )
    else:
        await message.answer("Sorry!It is allowed just for ADMIN1!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")





































