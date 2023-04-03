from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor


from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat


TOKEN = "your token"
logging.basicConfig(level=logging.INFO)


# прокси	
proxy_url = "http://proxy.server:3128"


bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


# Функция (запуск бота)
async def on_startup(dp):
	await bot.send_message(your id, "Я запустился")

# Функция (выключение бота)
async def on_shutdown(dp):
	await bot.send_message(your id, "Я завершил работу")



# Менюшка команд бота
async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
		"ru": [
			BotCommand("start", "Команда start запускает бота, начать сначала"), # /start
			BotCommand("help", "Вывести информацию по боту"), # /help
			BotCommand("id", "Узнать свой id"), # /id
			BotCommand("echo", "Эхо"), # /echo
			BotCommand("games", "Узнать какие есть игры"), # /games
		],
		"en": [
			BotCommand("start", "Restart bot"), # /start
			BotCommand("help", "Info about bot"), # /help
			BotCommand("id", "Find your id"), # /id
			BotCommand("echo", "Echo"), # /echo
			BotCommand("games", "Find out what games are available"), # /games
		]
	}
    for language, commands in STARTING_COMMANDS.items():
	    await bot.set_my_commands(
		    commands=commands,
		    scope=BotCommandScopeChat(chat_id),
		    language_code=language
		)


# /start
# 1 меню выбор языка
@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)
    await set_starting_commands(bot, message.from_user.id)


# /help
@dp.message_handler(commands="help")
async def command_help(message: types.Message):
    if message.from_user.language_code == "ru":
	    await message.answer("Вы можете использовать меня для загрузки игр, посмотреть наш Youtube, Discord и т.д.😲")

    elif message.from_user.language_code == "en":
	    await message.answer("You can use me for download games, see our Youtube, Discord etc.😲")


# /id
@dp.message_handler(commands="id")
async def command_id(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer(f"Ваш id: {message.from_user.id}")

    elif message.from_user.language_code == "en":
	    await message.answer(f"Your id: {message.from_user.id}")


# /echo
@dp.message_handler(commands="echo")
async def command_echo(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("Если отправить что-то из этого списка\n1. Смайлик\n2. Эмоджи\n3. Gif\n4. Видео\n4. Фото\n5. Голосовое сообщение\n\nБот отправит вам его в ответ")

    elif message.from_user.language_code == "en":
        await message.answer("If you send something from this list\n1. Smiley face\n2. Emoji\n3. Gif\n4. Video\n4. Picture\n5. Voice message\n\nBot will send it back to you")


# /games
@dp.message_handler(commands="games")
async def command_games(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Horror\n2. ES MOD\n\nWEB GAMES\nПока нет")

    elif message.from_user.language_code == "en":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Horror\n2. ES MOD\n\nWEB GAMES\nNot yet")



# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)