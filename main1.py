from aiogram.utils import executor
from config1 import dp
from heandlers1 import admin1, client1, callback1, extra1
import logging
async def on_startup(_):
    print('Bot is online!')


admin1.register_handlers_admin(dp)
client1.register_handlers_client(dp)
callback1.register_handler_callback(dp)
extra1.register_hendler_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
