# TEXT to SQL

- Here it write a well written sql query for fetching data from database
- It wont run sql to database, just creates SQL Statement
- Used OpenAI **gpt-3.5-turbo** AND **ChatGeneration** to get the response
- Create a ChatGeneration to enable the prompt playground
- **Reference:** https://docs.chainlit.io/examples/openai-sql

# ---------------------------------------------------------------------------

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp310 python=3.10 -y

```

```bash
conda activate llmapp310
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your OPENAI_API_KEY credentials as follows:

```ini
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
chainlit run app.py
```

Now,

```bash
open up localhost:  http://localhost:8000/
```
