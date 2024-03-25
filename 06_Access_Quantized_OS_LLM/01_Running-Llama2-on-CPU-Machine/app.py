from flask import Flask, render_template, jsonify, request
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import CTransformers
from src.helper import *

# Initialize the flask
app = Flask(__name__)


# Load the PDF File
loader = DirectoryLoader("data/", glob="*.pdf", loader_cls=PyPDFLoader)

documents = loader.load()


# Split Text into Chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
text_chunks = text_splitter.split_documents(documents)


# Load the Embedding Model via hugging face
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
)  # Download to cpu


# Create Local Vector DB
# Convert the Text Chunks into Embeddings and Create a FAISS Vector Store - This is local embedding like Chroma db
# Just we need to pass text chunks and embedding models
vector_store = FAISS.from_documents(text_chunks, embeddings)


# Beforehand downloaded llama-2-7b-chat.ggmlv3.q4_0.bin inside model folder
# Call quantized LLM llama-2 model - model/llama-2-7b-chat.ggmlv3.q4_0.bin
# This is quantized model loading, so use CTransformers
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 128, "temperature": 0.01},
)

# Create PromptTemplate and pass ["context", "question"] to template variable in src/helper.py
qa_prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# Use langchain RetrievalQA object and use LLM model and pass vector_db output and custome prompt template also
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": qa_prompt},
)


# Flask main page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", **locals())


# Gets user input as question and passes this to chain and Returns the response to html page
@app.route("/chatbot", methods=["GET", "POST"])
def chatbotResponse():

    if request.method == "POST":
        user_input = request.form["question"]
        print(user_input)

        # passes this to chain
        result = chain({"query": user_input})
        print(f"Answer:{result['result']}")

    # Returns the response to html page
    return jsonify({"response": str(result["result"])})


# Intialize the application. Scripts starts here
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)  # Its running in local host 8080
