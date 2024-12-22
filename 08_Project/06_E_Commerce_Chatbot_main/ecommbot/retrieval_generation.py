# In this script it Retrives info from Astra DB Based on User Q and system prompt which we defined.

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# from langchain_openai import ChatOpenAI #If use OpenAI, uncomment it
from langchain_google_genai import ChatGoogleGenerativeAI

from ecommbot.ingest import ingestdata


def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
    Your ecommercebot bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    # llm = ChatOpenAI()  #Initialize OpenAI model
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")  # gemini-1.5-pro

    # print("llm model: ", llm)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


if __name__ == "__main__":
    vstore = ingestdata(
        "done"
    )  # Already done this step in the dev time,"done"-->Vectore store already created, so directly use vstore data, No need ingestion"
    chain = generation(vstore)
    print("\nResponse:\n", chain.invoke("can you tell me the best bluetooth buds?"))
