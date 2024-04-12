# Main Telegram Bot Code,

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai  # To ans any Q

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Read API_Key of Telegrambot
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Read API_Key of OPENAI_API_KEY

# Connect with OpenAI
openai.api_key = OPENAI_API_KEY

# print("Ok")

MODEL_NAME = "gpt-3.5-turbo"  # Using this Openai model

# Initialize Telegram bot
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


class Reference:
    def __init__(self) -> None:
        self.response = ""


# Initialize the Reference class, its going to be used as memory
# All the conversation will be saved here
reference = Reference()


# Clear the response variable to make conversation history as Null
def clear_past():
    reference.response = ""


# Here it calls clear_past() function and deletes all memory of conversation when it gets /clear word
@dispatcher.message_handler(commands=["clear"])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")


@dispatcher.message_handler(commands=["start"])
async def welcome(message: types.Message):
    """This handler receives messages with `/start` command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi\nI am a Chat Bot! Created by Prabha. How can i assist you?")


@dispatcher.message_handler(commands=["help"])
async def helper(message: types.Message):
    """
    This handler receives messages with `/help` command
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm a bot created by Prabha! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)


# This is main bot, it wont be taking any command, whatever message passed will becomes Q to LLM
@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    A handler to process the user's input and generate a response using the openai API.
    """

    print(f">>> USER: \n\t{message.text}")  # Printing User Q in terminal window

    # Here response is the output from the LLM Model
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},  # role assistant
            {"role": "user", "content": message.text},  # our query from Telegram
        ],
    )

    # Printing Full Response in terminal window
    print(f">>> Full resonse: \n\t{response}")

    reference.response = response["choices"][0]["message"]["content"]

    # Chat Id, its unique id created for each chat endpoint, if we ask 2 Q, both will have same chatid
    print("message.chat.id: ", message.chat.id)
    print(f">>> chatGPT: \n\t{reference.response}")

    await bot.send_message(chat_id=message.chat.id, text=reference.response)
    print


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
