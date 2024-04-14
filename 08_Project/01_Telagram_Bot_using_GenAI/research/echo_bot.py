# This is initial code, before creting modular script - telegram_bot.py

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Read API_Key of Telegrambot

# print(API_TOKEN)

# configure logging
logging.basicConfig(level=logging.INFO)  # Loginfo


# Initialize Telegram bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Here @dp is something like streamlit @st once its initialized
@dp.message_handler(commands=["start", "help"])
async def command_start_handler(message: types.Message):
    # Here async is python decorator
    """This handler receives messages with `/start` or  `/help `command and reply as
            Hi!\n I am an Echo Bot!\n Powered by Aiogram

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by Aiogram")


@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo message, means whatever message passed will display as echo in bot

    Args:
        message (types.Message): _description_
    """

    await message.reply(message.text)
    # await message.reply("Got it")


## Like Above We can create multiple function, Like Getting ans from LLM /RAG etc for telebot Q/Line

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    # This is the main executer, here we call Telegram dispatcher
    # Here skip_updates=True, If Bot is offline, it replies to message once its online
