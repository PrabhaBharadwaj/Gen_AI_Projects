# PII Masking

## Best Link:

- Try this **presidio/presidio_demo:** https://www.youtube.com/watch?v=RPJ3-kEUybU

  - **Code:** https://huggingface.co/spaces/presidio/presidio_demo/tree/main

- https://www.youtube.com/watch?v=MYxPDgnZIts

  - Code: 01_De-identification_Presidio.ipynb and 02_Detect_AI_Generated_Content.ipynb

- **Anonymization with LangChain and Presidio**

  - https://dev.to/rutamstwt/langchain-data-protection-op9
  - https://python.langchain.com/v0.2/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.presidio.PresidioReversibleAnonymizer.html

- **Databaricks**
  - https://github.com/andyweaves/databricks-notebooks/tree/main/notebooks/privacy
  - 
- Presidio can be a good start for the POC. However, it has limitations.

Presidio contains predefined recognizers for various PII entities, including:

- Credit card numbers

- Crypto wallet numbers (currently only Bitcoin addresses are supported)
- Date and time information
- Email addresses
- IBAN codes
- IP addresses
- Nationality, religious, or political group information (NRP)
- Location information
- Person names
- Phone numbers
- Medical license numbers
- URLs
  For production purposes, it would be good to explore and integrate with 3rd party providers like private-ai
