### Install library
pip install pymupdf
pip install langchain_community
pip install langchain_core
pip install langchain_openai


# Set up your API key:

export OPENAI_API_KEY=’your_openai_api_key’

# The Code: A Closer Look
import base64
import logging
from sys import argv

import pymupdf
from langchain_community.callbacks import get_openai_callback
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableSerializable

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def system_prompt() -> str:
    return """You are an expert in optical character recognition (OCR) specializing in converting PDF images to Markdown format. 
Your task is to analyze images of PDF pages, accurately transcribe their content into well-structured Markdown. 
Follow these guidelines:

1. Examine the provided image(s) of PDF page(s) carefully.
2. Extract all text content from the image(s).
3. Convert the extracted text into properly formatted Markdown, preserving the original structure and layout.
4. Use appropriate Markdown syntax for headings, lists, tables, and other formatting elements.
5. For complex equations or formulas, use LaTeX syntax enclosed within $$ delimiters.
6. If there are images or diagrams, indicate their presence with a brief description in square brackets, e.g., [Image: diagram of a cell].
7. Maintain the logical flow and organization of the original document in your Markdown representation.
8. Return only the Markdown content without any additional explanations or markdown code block delimiters.

Proceed with the OCR and Markdown conversion task based on these instructions."""


def get_markdown_conversion_chain() -> RunnableSerializable:
    logger.info("Initializing the markdown conversion chain.")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt()),
            (
                "user",
                [
                    {
                        "type": "image_url",
                        "image_url": {"url": "data:image/jpeg;base64,{image_data}"},
                        "detail": "high",
                    }
                ],
            ),
        ]
    )
    return prompt_template | llm | StrOutputParser()


def pdf_to_base64(pdf_path: str) -> list[str]:
    logger.info(f"Converting PDF at {pdf_path} to base64.")
    with pymupdf.open(pdf_path) as pdf_file:
        base64_pages = [
            base64.b64encode(page.get_pixmap().tobytes()).decode("utf-8")  # type: ignore
            for page in pdf_file
        ]
    logger.info(f"Converted {len(base64_pages)} pages to base64.")
    return base64_pages


def convert_pdf_to_markdown(pdf_paths: list[str]) -> list[str]:
    logger.info("Starting PDF to Markdown conversion process.")
    markdown_conversion_chain = get_markdown_conversion_chain()
    markdown_documents = []
    for path in pdf_paths:
        logger.info(f"Processing PDF: {path}")
        base64_pages = pdf_to_base64(path)
        markdown_pages = markdown_conversion_chain.batch(
            [{"image_data": page} for page in base64_pages]
        )
        markdown_documents.extend(markdown_pages)
    logger.info("PDF to Markdown conversion process completed.")
    return markdown_documents


if __name__ == "__main__":
    logger.info("Script execution started.")
    with get_openai_callback() as callback:
        response = convert_pdf_to_markdown(argv[1:])
        output_path = "src/output/markdown.md"
        with open(output_path, "w") as output_file:
            output_file.write("\n".join(response))
        logger.info(f"Markdown content written to {output_path}.")
        print(callback)
    logger.info("Script execution finished.")