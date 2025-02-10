# Vision Model - Revolutionizing OCR: Harnessing GPT Vision Models for PDF-to-Markdown Conversion

Link: https://medium.com/@varungangu1/revolutionizing-ocr-harnessing-gpt-vision-models-for-pdf-to-markdown-conversion-aef97ec7468c#:~:text=PDF%20Processing%3A%20The%20script%20reads,OCR%20to%20extract%20the%20text.

Code: https://github.com/samwit/ollama-tutorials/blob/main/ollama_python_lib/ollama_scshot_annotator.py

- Let’s break down the key components of our script:

- System Prompt: We define a detailed prompt that instructs the GPT Vision model on how to perform OCR and convert the text to Markdown.
- Markdown Conversion Chain: We set up a conversion chain using ChatOpenAI, which processes the base64-encoded PDF images and produces Markdown output.
- PDF-to-Base64 Conversion: Each page of the PDF is converted into a base64-encoded string for processing.
- PDF-to-Markdown Conversion: The core function processes each encoded PDF page through the conversion chain.
- Main Execution: The script handles command-line arguments, processes the PDFs, and writes the generated Markdown to an output file.
- Results and Performance
- In our tests, we processed a three-page PDF using both GPT-4o and GPT-4o-mini models. The results were impressive:

- GPT-4o-mini: Cost approximately $0.01 for three pages
- GPT-4o: Cost approximately $0.05 for three pages
- Both models successfully captured formulas and tables in the proper format, with GPT-4o showing slightly better output quality.
