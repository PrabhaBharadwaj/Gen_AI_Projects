from src.helper import repo_ingestion, load_repo, text_splitter, load_embedding
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
import os

# dotenv to read .env's OPENAI_API_KEY
load_dotenv()

# Read OPENAI KEY from .env
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# load_repo is Loading repositories as documents
documents = load_repo("repo/")

# Creating text chunks
text_chunks = text_splitter(documents)

# loading OpenAIEmbeddings model
embeddings = load_embedding()


# storing vector in choramdb
vectordb = Chroma.from_documents(
    text_chunks, embedding=embeddings, persist_directory="./db"
)
vectordb.persist()
