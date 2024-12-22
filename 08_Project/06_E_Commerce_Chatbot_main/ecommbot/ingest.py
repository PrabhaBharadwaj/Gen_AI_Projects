# This script will load list of document format data to Astra DB and applies embedding on data and stores in vector format

from langchain_astradb import AstraDBVectorStore

# from langchain_openai import OpenAIEmbeddings #If use OpenAI, uncomment it
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
import os
import pandas as pd
from ecommbot.data_converter import dataconveter

# from langchain_core.pydantic_v1 import BaseModel
from pydantic import BaseModel

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

## OpenAI embedding
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

## If use Gemin embedding
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


print("Use GOOGLE_API_KEY embedding")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
print("embeddings:", embeddings)


def ingestdata(status):
    # Define AstraDBVectorStore
    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="chatbotecomm",  # New Collection nmae in Astradb
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )

    storage = status

    if storage == None:
        print("\nVectore store not created, so ingest data")
        docs = dataconveter()
        inserted_ids = vstore.add_documents(docs)
    else:
        print(
            "\nVectore store already created, so directly use vstore data, No need ingestion"
        )
        return vstore
    return vstore, inserted_ids


# If we kept in __name__ == "__main__, it execute that part 1st
if __name__ == "__main__":
    vstore, inserted_ids = ingestdata(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")
