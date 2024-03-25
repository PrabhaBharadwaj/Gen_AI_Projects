# This is a helper file, all commonly used variables etc kept here and accessed in main.py/app.py


# This DEFAULT_SYSTEM_PROMPT prompt used to show basic prompts in run_local.py file
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. 
Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of 
answering something not correct. If you don't know the answer to a question,
please don't share false information."""


# This CUSTOM_SYSTEM_PROMPT prompt used to show customized system prompts in run_local_1.py file

# CUSTOM_SYSTEM_PROMPT="You are an advanced assistant that provides translation from English to French"
CUSTOM_SYSTEM_PROMPT = (
    "You are an advanced assistant that provides summarization given any book name"
)

# This template prompt used in main file main.py/app.py
# Create another Prompt for QA, it will be called inside app.py

template = """Use the following pieces of information to answer the user's question.
If you dont know the answer just say you know, don't try to make up an answer.

Context:{context}
Question:{question}

Only return the helpful answer below and nothing else
Helpful answer
"""
