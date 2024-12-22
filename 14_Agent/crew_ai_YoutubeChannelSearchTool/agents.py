from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

import os

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"  # "gpt-4-0125-preview"

# OpenAI gives token limit error, so trying google api key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
## call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


## Create a senior blog content researcher
# This agent responsibe for read youtube content, Define role here
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video transcription for the topic {topic} from the provided Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"
    ),
    tools=[yt_tool],
    llm=llm,  # Here we are using gemini model, so we need to define llm here, else it takes defaut OPENAI_MODEL_NAME and OPENAI_API_KEY
    allow_delegation=True,
)

## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,  # Here we are using gemini model, so we need to define llm here, else it takes defaut OPENAI_MODEL_NAME and OPENAI_API_KEY
    allow_delegation=False,
)
