from crewai import Crew, Process  # Crew ai main library
from agents import blog_researcher, blog_writer  # Custom created library
from task import research, write  # Custom created library


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],  #
    tasks=[research, write],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

## start the task execution process with enhanced feedback
result = crew.kickoff(  # Here inputs we will pass Q/ Topcic to be checked
    inputs={
        "topic": "Realtime Multimodal RAG Usecase Part 3 | MultiVectorRetriever with Langchain | RAG Application"
    }
)
print(result)
