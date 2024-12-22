# AGENTS

- This agent responsibe for read Google content using **SERPAPI** AND writes content in .md file
- We created **Research** and **Writing** task agents
- This tried in loacl VDI

## STEPS:

- Create new python venv. Crew AI need version python>=3.11

```
conda create -p venv_new python=3.11 -y

conda activate "D:\Prabha\Data Science\Prabha-DS\Gen_AI\Ineuron\Gen_AI_Course\Project\venv_new"
```

- If already existing venv activate

```
conda activate  "D:\Prabha\Data Science\Prabha-DS\Gen_AI\Ineuron\Gen_AI_Course\Project\venv"
```

- Install requirements.txt

```
pip install -r requirements.txt
```

- For Crew script, agent and task files are required

- **Agents**

  - Here define agents.
  - This agent responsibe for read youtube content, Define role here
  - We defined 2 agents.
    - **1.blog_researcher:** Get the relevant video transcription for the topic {topic} from the provided Yt channel
    - **2. blog_writer:** Narrate compelling tech stories about the video {topic} from YT video

- **tool**

  - Define the tool here. Crewai has inbuild YoutubeChannelSearchTool, which search from Youtube
  - Just mention youtube channel name

- **task:**

  - Define the task here. Provide tools to use which defined in tools.py and agents to use which defined in agent.py. Mention the output_file if any
  - We define 2 task.
    - **1. Research Task:** Get detailed information about the video from the channel video.
    - **2. Writing task with language model configuration:** get the info from the youtube channel on the topic {topic}.

- **crew:**

  - Forming the tech-focused crew with some enhanced configurations
  - Here we initialize crew by passing agents list and tasks list

- **Execute**
- Execute below statement. But now getting below error due to openai tiken limit issue
- When it executes it create db folder, default creates chrom db

  ```
    python crew.py

  ```

  ```
    raise self._make_status_error_from_response(err.response) from None
  openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
  ```
