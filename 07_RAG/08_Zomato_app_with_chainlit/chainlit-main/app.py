import chainlit as cl
from src.llm import ask_bot  # Main body of the bot where LLM called and logic written
from src.config import instruction  # To Import Prompt/Sytem behaviour


@cl.on_message
async def main(user_message: cl.Message):

    response = ask_bot(user_message.content, instruction)

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response}",
    ).send()
