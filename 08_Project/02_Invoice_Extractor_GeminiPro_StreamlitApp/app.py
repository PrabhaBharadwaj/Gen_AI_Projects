# Invoice Extractor using Gemini Pro - Q&A Chatbot

# from langchain.llms import OpenAI

from dotenv import load_dotenv  # To read env variable

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

# Conncet to Google API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to load gemini-pro-vision  model and get respones
def get_gemini_response(input_prompt, image, user_question):
    """_summary_

    Args:
        input_prompt (Text): This is like system prompt, we will tell model to behave like invoice extractor
        image (Image): Invoice Image
        user_question (Text): Question we are asking as a user on invoice in webpage

    Returns:
        response(Text): Response from model
    """
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input_prompt, image[0], user_question])
    return response.text


## Function to Read the image file into bytes
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:

        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app
st.set_page_config(page_title="Gemini Pro Vision basic Demo - Invoice Extractor")

st.header("Gemini Application  Invoice Extractor")
user_question = st.text_input("Input Prompt: ", key="user_question")  # User Q
uploaded_file = st.file_uploader(
    "Choose an image of the Invoice:", type=["jpg", "jpeg", "png"]
)
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Read Image

    # Display Image in Webpage
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# This is like system prompt
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)  # Convert image to Byte
    response = get_gemini_response(input_prompt, image_data, user_question)
    st.subheader("The Response is")
    st.write(response)
