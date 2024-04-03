# Import all libraries and internal package from helper.py
from langchain.vectorstores import Chroma
from src.helper import load_embedding
from dotenv import load_dotenv
import os
from src.helper import (
    repo_ingestion,
)  # repo_ingestion is a function created to clone the repo
from flask import Flask, render_template, jsonify, request
from langchain.chat_models import (
    ChatOpenAI,
)  # Here we call default openai model gpt 3.5 turbo
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain

# Initialize the flask
app = Flask(__name__)

# dotenv to read .env's OPENAI_API_KEY
load_dotenv()

# Read OPENAI KEY from .env
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# loading OpenAIEmbeddings  model, This function written in helper.py
embeddings = load_embedding()
persist_directory = "db"

# Invoke already created Knowledge base from CHROMA db folder. This is the embedding info of Cloned repo
# Now we can load the persisted database from disk, and use it as normal.
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Here we call default openai model gpt 3.5 turbo - ChatOpenAI()
llm = ChatOpenAI()  # We can specify other than default model inside ()

# Create ConversationSummaryMemory by passing llm
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)

# Create Chain - ConversationalRetrievalChain passing llm, ectordb.as_retriever, memory
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=vectordb.as_retriever(
        search_type="mmr", search_kwargs={"k": 8}  # Retrives top 8 similarity chunks
    ),
    memory=memory,
)


# Basic 1st page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# Here ask 1st Prompt to pass repo details
@app.route("/chatbot", methods=["GET", "POST"])
def gitRepo():

    if request.method == "POST":
        user_input = request.form["question"]  # Here we pass Git repo link
        repo_ingestion(
            user_input
        )  # This git repo link will be passed to repo_ingestion and saved inside repo folder
        os.system("python store_index.py")

    return jsonify({"response": str(user_input)})


# Here ask 2nd Prompt to ask Q on knowledge base
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    if input == "clear":  # If Q/msg = clear then clears knowldge base/delete rep folder
        os.system("rm -rf repo")
        print("Knowledge base cleared")
        return str("Knowledge base cleared")
    else:

        result = qa(input)
        print(result["answer"])
        return str(result["answer"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
