# Basic Langchain Code

LangChain is a framework for developing applications powered by language models.

- GitHub: https://github.com/hwchase17/langchain
- Docs: https://python.langchain.com/en/latest/index.html

- In simple **lagchain** if we give any query langchain uses its **own embedding** and converts to **vector and feeds to LLm**

- Holds Calling OpenAI API, HuggingFace API, Gemini(Google) API Connection examples from **Langchain**

### Overview:

- **Installation**
- **Setup the environment**
- **LLMs** (Connct to different LLM using API_KEY via langchain)
  - Tried **OPENAI** and **HuggingFace** LLM model using API_Keys
- **Prompt Templates** (It provides template for llm prompt)
  - **\*prompt template** used when we have **same template multiple time**
  - Normally when you use an LLM in an application, you are not sending user input directly to the LLM. Instead, you need to take the user input and construct a prompt, and only then send that to the LLM.
- **Chains** (Chains of prompt)

  - Combine LLMs and Prompts in multi-step workflows
  - Provided example Without Chain running one after the other
    - **5.1. Simple Sequential Chain**
      - Combine Multiple PromptTemplates
      - The output from the **first PromptTemplate is passed to the next PromptTemplate** as input
      - Only **final prompt** output displayed
    - **5.2. Sequential Chain**
      - Its same as **simplesequentialchain** just difference is here, we define **output_key**, so simple seq gives only last o/p , this gives both
      - If we want **all** the prompt output then use **Sequential Chain**

- **Agents** (With the help of agents, we are accessing Tools) and Tools (Tools which we are using Serpapi,wikipedia)

  - Whenever we want **real time data** which is not there in LLM(Which trained using old data), then only we use Agents. If data is fixed then we use RAG
  - Agent will conenct with **external tools** and it will use LLM reasoning capabilities
  - All the tools like **Google Search Tool and Math Tool are available as part of LangChain and you can configure agent, so agent is nothing but using all these tools and LLM reasoning capabilities** to perform a given task
  - To access Google Search Results in Real Time we use **serpapi**

    - **Tool:** A function that performs a specific duty. This can be things like: Google Search, Database lookup, Python REPL, other chains.
    - **LLM:** The language model powering the agent.
    - **Agent:** The agent to use.

  - **6.1 AGENT: serpapi(Google serach) and llm-math tool**
  - **6.2 AGENT: Wikipedia and llm-math tool**
    - **Wikipedia is open source api**, so while reading this we doesn't mention any API KEY, BUT **Serpapi** key used for **Google search** just **load_tool name will change from serpapi or wikipedia**
  - **6.3 AGENT: Human as a tool**
    - Here it ask human for ans the Q

- **Memory** (Remembering Chat History) - We can attach memory to remember all previous conversation

      - **Conversation chain** and **Conversation buffer memory** are same only, It keep on adds content/ q&a respnse to memory, keeps growing

      - **7.1 ConversationBufferMemory**
          - We can attach memory to remember all previous conversation.  Conversation buffer memory goes growing endlessly, It takes huge space

      - **7.2 ConversationChain**

      - This is same like **Conversation buffer memory**, It keep on adds content/ q&a respnse to memory, keeps growing
      - It behaves like AI and human conversation


      - **7.3 ConversationBufferWindowMemory**

      - Conversation buffer memory and ConversationChain goes growing endlessly, It takes huge space
      - It  Just remember last 5 Conversation Chain based on we set parameter k=5
      - It Just remember last 10-20 Conversation Chain based on we set parameter k=10/20

- **Document Loaders** (Load our PDF file)

  - Load the pdf file via langchain framework
  - Langchain **Document Loader** converts any type(.pdf,.csv .json etc) format data and converts as **document**
  - https://python.langchain.com/docs/modules/data_connection/document_loaders/
    - By using this **Document loader** we can read any format document and then split into **chunks** and use **embedding** to convert to vector and save in **vector db** then do **retrival(RAG)** operation

- **Indexes**
