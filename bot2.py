# Импорт библиотек
import random
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


# Ссылки на файлы на компе
ben_yes = open("ben-yes-yes.mp4", 'rb')
ben_no = open("dog-saying-no-no.mp4", 'rb')
ben_close = open("brosil.mp4", 'rb')
ben_hoho = open("ben-hoho.mp4", 'rb')
ben_zvonok = open("zvonok.mp4", 'rb')

# Листы
lst = list()
lst_call = list(ben_zvonok)
lst_bye = list(ben_close)


lst.append(ben_yes)
lst.append(ben_no)
lst.append(ben_hoho)





#dict = {'ben_hoho':'https://drive.google.com/file/d/1Athicu8Rd3rnePa-5lmBoc81VUb0s-Ay/view?usp=sharing'}


bot = Bot(token='5252868130:AAE7MiOUoWJw0fufrSoXL7a_WzRhXnUY2kI')
dp = Dispatcher(bot)


# Хендлер для старта
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Прочитай /help и задавай вопрос!")


# Хендлер для хелпы
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Пиши после того как загрузится и не 4 символа!!! \n Позвонить - /call \n Бросить трубку- /bye ")


# Хендлер для начала звонка
@dp.message_handler(commands=['call'])
async def process_call_command(message: types.Video):
    await bot.send_video(message.from_user.id, random.choice(lst_call))


# Хендлер для конца звонка
@dp.message_handler(commands=['bye'])
async def process_bye_command(message: types.Video):
    await bot.send_video(message.from_user.id, random.choice(lst_bye))


# Хендлер для ловли всех сообщений
@dp.message_handler()
async def all_message_command(message: types.Video):
    await bot.send_video(message.chat.id, random.choice(lst))


#@dp.message_handler()
#async def all_message_command(message: types.Video):
#    await bot.send_video(message.chat.id, random.choice(dict))


#if __name__ == '__main__':
    #executor.start_polling(dp)


executor.start_polling(dp)
