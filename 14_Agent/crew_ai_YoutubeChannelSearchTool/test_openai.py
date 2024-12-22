# This created t test Openai connectoion

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

os.environ["OPENAI_API_KEY"] = (
    "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"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": [{"type": "text", "text": "hi\n"}]},
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "Hello! How can I assist you today?"}],
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Hello! How can I help you today? If you have any questions or need assistance, feel free to ask.",
                }
            ],
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "which model re you using\n"}],
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "As an AI developed by OpenAI, I don't have a specific model name like consumer products do. I am based on the GPT (Generative Pre-trained Transformer) architecture and updated regularly with improvements and new data up to my knowledge cutoff in September 2021. If you're asking about the specific version of the model, it is a variant of the GPT-3 model, which is one of the most advanced AI language models available as of my last update. Please note that OpenAI continuously works on improving AI models, so there might be newer models or versions that have been released after my last update.",
                }
            ],
        },
    ],
    response_format={"type": "text"},
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print("Response:n", response)
