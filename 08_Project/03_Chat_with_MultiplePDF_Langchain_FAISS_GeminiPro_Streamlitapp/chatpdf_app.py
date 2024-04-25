import streamlit as st
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# get_pdf_text  to read pdf's as text; get_text_chunks to convert text to chunks; get_vector_store to convert chunk to vector db
from src.helper import get_pdf_text, get_text_chunks, get_vector_store

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Create conversational_chain
def get_conversational_chain():
    """
    Create prompt_template and then
    Create Conversational chain, Pass prompt template to Langchain's load_qa_chain with LLM Model

    Returns:
        chain: Its Final Langchain Chain
    """

    # Create System prompt template by passing Vectordb similarity searched Context and User Question
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # Initiate LLM Model gemini-pro
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Create Langchain's Prompt tempalte
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    # Add Conversation buffer memory
    memory = ConversationBufferMemory(memory_key="chat_history", input_key="question")

    # We can use ConversationalRetrievalChain or load_qa_chain(Can use prompttemplate), both has different code
    chain = load_qa_chain(
        model, chain_type="stuff", prompt=prompt, memory=memory
    )  # stuff - It helps Internal text summarization

    return chain


def user_input(user_question):
    """
    This is Final Function, which passes User Q to already created Vector db and pass to LLM Chain and get the response

    Args:
        user_question (Text): User Question on PDF

    Return:
        None: Print the Response in Stramlit webpage
    """

    # Using same embedding to call FAISS Saved index/vectore db=faiss_index
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Load the Earlier saved vectordb=faiss_index_db
    new_db = FAISS.load_local(
        "faiss_index_db", embeddings, allow_dangerous_deserialization=True
    )

    # Apply similarity_search on user_question and get the context
    docs = new_db.similarity_search(user_question)

    # Call chain
    chain = get_conversational_chain()

    # Get response from LLM Chain
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True,
    )  # Here input_documents is defaault parameter of load_qa_chain - chain clas
    # "chain.run(input_documents=reordered_docs, query=query)"

    # Print the Response here
    print(response)
    # Print the Response in Stramlit webpage
    st.write("Chatbot Reply: ", response["output_text"])


# Main Function, which starts Streamlit frontend
def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    # Create Side bar in streamlit to upload pdf's. 1st upload pdfs and submit, then ask User Q
    with st.sidebar:
        st.title("Menu:")
        # Upload PDF Files here
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button",
            accept_multiple_files=True,
        )
        if st.button("Submit & Process"):
            # Once User uploads files and press "Submit & Process", it does all embedding andd vector db creation
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

    # Ask User Q and press enter then this executed
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        # Calls main function andPrint the Response in Stramlit webpage
        user_input(user_question)


# Call main function 1st
if __name__ == "__main__":
    main()
