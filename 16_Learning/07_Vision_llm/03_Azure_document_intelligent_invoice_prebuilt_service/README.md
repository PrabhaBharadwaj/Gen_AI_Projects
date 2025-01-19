# Azure Document Intelligent

## Reference:

- **Evaluating the quality of AI document data extraction with small and large language models with Azure Document Intelligent:**

  - https://techcommunity.microsoft.com/blog/azureforisvandstartupstechnicalblog/evaluating-the-quality-of-ai-document-data-extraction-with-small-and-large-langu/4157719
  - https://learn.microsoft.com/en-us/samples/azure-samples/azure-ai-document-processing-samples/document-processing-with-azure-ai-samples/
  - **Data Extraction - Azure AI Document Intelligence + Phi-3.5 MoE:**
    - https://github.com/azure-samples/azure-ai-document-processing-samples/blob/main/samples/extraction/text-based/document-intelligence-phi.ipynb
  - **Data Extraction - Azure AI Document Intelligence + Azure OpenAI GPT-4o:**
    - https://github.com/Azure-Samples/azure-ai-document-processing-samples/blob/main/samples/extraction/text-based/document-intelligence-openai.ipynb

  ## Models and Techniques

  - This evaluation focused on multiple techniques for data extraction with the language models:

  - **Markdown Extraction with Azure AI Document Intelligence.** This technique involves converting the document into Markdown using the pre-built layout model in Azure AI Document Intelligence. Read more about this technique in our detailed article.
  - **Vision Capabilities of Multi-Modal Language Models.** This technique focuses on GPT-4o and GPT-4o Mini models by converting the document pages to images. This leverages the models’ capabilities to analyze both text and visual elements. Explore this technique in more detail in our sample project.
  - **Comprehensive Combination.** This technique combines both Markdown extraction with vision capable models to enhance the extraction process. Additionally, the layout analysis of Azure AI Document Intelligence will ease the human review of a document if the confidence or accuracy is low.

- **Refer video**(This also has python code, but no repo given):

  - https://www.youtube.com/watch?v=Ry4VAesjU4I

- **Other Python code:**
  - https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Prebuilt_model/sample_analyze_invoices.py
  - https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Prebuilt_model/sample_analyze_receipts.py
