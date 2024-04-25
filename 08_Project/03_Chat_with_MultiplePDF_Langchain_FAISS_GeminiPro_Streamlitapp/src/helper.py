# Here we keep all main helper functions
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Using Gemin's embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_pdf_text(pdf_docs):
    """Read all PDF in our local folder/Passed in webpage and create as 1 document

    Args:
        pdf_docs (Document): Reads each pdf and Read each pages in pdf and append as text

    Returns:
        text: Returns final text document by combining all pdf content
    """
    text = ""
    # Read each psf doc
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        # Read each pages in pdf
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    """Split document into Chunks by defining chunk_size

    Args:
        text (text): Pass the whole document

    Returns:
        None:
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    """Pass text chunks and apply Google's embedding model(embedding-001)
        Save the vector in Local FAISS Vector  db as faiss_index(Inside faiss_index local folder)

    Args:
        text_chunks (Text): Pass text chunks
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(
        "faiss_index_db"
    )  # Load the Earlier saved vectordb=faiss_index
