# Import all library
from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

# Insruction Token and System Token
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

# Insruction Token
instruction = "Convert the following text from English to hindi: \n\n {text}"

# Here using Default system Prompt which pased in helper.py
SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

# Combine SYSTEM_PROMPT + instruction Prompt as template
template = B_INST + SYSTEM_PROMPT + instruction + E_INST

# Create PromptTemplate
prompt = PromptTemplate(template=template, input_variables=["text"])

# Beforehand downloaded llama-2-7b-chat.ggmlv3.q4_0.bin inside model folder
# Call quantized LLM llama-2 model - model/llama-2-7b-chat.ggmlv3.q4_0.bin
# This is quantized model loading, so use CTransformers

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 128, "temperature": 0.01},
)


# Use LLMChain to pass prompt and llm
LLM_Chain = LLMChain(prompt=prompt, llm=llm)

# Inference with text
# print(LLM_Chain.run("How are you?"))
print(LLM_Chain.run("Harry Potter?"))
