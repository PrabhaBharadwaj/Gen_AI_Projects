# AZURE BASIC SETUP - AZURE AI STUDIO

![plot](./Images/

- https://portal.azure.com/#home
- Do azure subscription
- Open Azure OpenAI service and create the resource by selection region

**Create Azure AI Studio**

- Create Azure AI studio - AzureHub
- During creation tag Azure openAI service if its already created is available, else create new one
- Then press Review and Create to create "Azure AI studio"

**Create PROJECT inside Azure AI Studio**

- Create PROJECT inside Azure AI studio

  ![plot](./images/6_inside_azure_ai_studio.png)

- Inside PROJECT we can see, all different tabs like Databrics. Model catalog, playground, Model benchmark(It shows all different LLM model's benchmark score on different benchmark), Fine Tuning, under asset- Model Endpoint, data index etc.
  ![plot](./images/7_project_inside_azure_ai_studio.png)

- **Add new connection**
- https://learn.microsoft.com/en-us/azure/ai-studio/how-to/connections-add
- Then connect Azure Open AI service which we created earlier class, there we downloaded gpt4 model and created endpoint for that model.
- Follow this step inside Azure AI Studio's
  - Azure AI Studio --> Setting --> New Connection
    ![plot](./images/8_add_connection_in_azure_ai_studio.png)
- But now to some new enahancement this setting not visble in Azure AI studio. Copied some snapshot from video

  ![plot](./images/9_add_openai_connection_in_azure_ai_studio.png)

  ![plot](./images/10_add_openai_connection_in_azure_ai_studio.png)

  ![plot](./images/11_added_openai_connection_in_azure_ai_studio.png)

- After this we can invoke GPT4 model, which deployed in Azure OpenAI service in Azure AI studio.

## Build RAG in playground using already created/deployed Azure OpenAI endpoint

- Showed how to Create RAG inside AZURE AI Studio UI using Azure AI search service and Azure OpenaAI service's embedding model .
- Once its done, copied that backend code and executed that in local, so It does same RAG in local, which calls the same RAG Knowledge base and does inference. Code link: https://github.com/sunnysavita10/AzureOpenAI-Crash-Course/blob/main/app.py
- In above github, he has mutiple subfolder, there he has kept some sample code to use azure openai endpoint anddo the finetuning, voice data, function calling etc
  **12_RAG_in_playground**

  ![plot](./images/12_RAG_in_playground.png)

**13_RAG_backend_code**

![plot](./images/13_RAG_backend_code.png)

**14_RAG_prompt_flow**

- Showed promptflow, which helps to do endtoend pipeline which we done in playground setup. and showed deployment.

  ![plot](./images/14_RAG_prompt_flow.png)

**Azure_service**

![plot](./images/Azure_service.png)

**Cost_analysis**

![plot](./images/Cost_analysis.png)
