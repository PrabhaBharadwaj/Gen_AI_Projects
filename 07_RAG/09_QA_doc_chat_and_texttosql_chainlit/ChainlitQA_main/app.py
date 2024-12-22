# Document QA chainlit basic app

## Import all libraries
import os
from typing import List
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import (
    ConversationalRetrievalChain,
)
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain.memory import ChatMessageHistory, ConversationBufferMemory

## Import Chainlit
import chainlit as cl

print("all_ok")

## Read .env and set OPENAI_API_KEY as environment variable
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


## Define Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)


###################### Chainlit Functionality will start  ############
###################### Read External file and create Chunks and save in Vectordb and create final chain  ############
@cl.on_chat_start
async def on_chat_start():
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!",
            accept=["text/plain"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...", disable_feedback=True)
    await msg.send()

    # Read a uploaded file
    with open(file.path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split the text into chunks
    texts = text_splitter.split_text(text)

    # Create a metadata for each chunk. Pass seq chunk no as source
    metadatas = [{"source": f"{i}-pl"} for i in range(len(texts))]

    # Create a Chroma vector store
    embeddings = OpenAIEmbeddings()
    docsearch = await cl.make_async(Chroma.from_texts)(
        texts, embeddings, metadatas=metadatas
    )

    # Keep the chat history inmemory using langchain.memory
    message_history = ChatMessageHistory()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    # Define the chain with memory
    chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        memory=memory,
        return_source_documents=True,
    )

    # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("chain", chain)  # Set chain as user_session


###################### User Q & A  ######################
## From here user Q&A will be handled using above created chain-ConversationalRetrievalChain
# If we find word async and await, then its asynchronous process
# Define main code inside function main


@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")  # Calls Chains from user_session
    cb = cl.AsyncLangchainCallbackHandler()

    res = await chain.acall(
        message.content, callbacks=[cb]
    )  # Here it passes Q to chain and retrives info and provides response
    answer = res["answer"]
    source_documents = res["source_documents"]

    text_elements = []  # type: List[cl.Text]

    # Here we will display all chunks/ sources which helpd to provide ans with context/chunk(text_elements)
    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            # Create the text element referenced in the message
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"  # Answer appended with source/chunk number
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()
    # Here answer displayed anong with text_elements/chunks/Context
