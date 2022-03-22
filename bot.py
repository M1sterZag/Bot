#pip install -U aiogram
#pip install emoji

# Импорт библиотек и токены со стартом бота
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot

logging.basicConfig(level=logging.INFO)



from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Хендлер ловит старт
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


# Хендлер ловит хелп
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# Хендлер ловит все и отправляет эхом
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)






#if __name__ == '__main__':
#    executor.start_polling(dp)
executor.start_polling(dp)