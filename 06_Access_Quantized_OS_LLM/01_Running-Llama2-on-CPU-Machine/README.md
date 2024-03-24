# Running-Llama2-on-CPU-Machine

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.8 -y
```

```bash
conda activate llmapp
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

## For Flask app:

- Copied some html template inside **templates/index.html** file
- Created some **static folder** and added **jquery.min.js** and copied some content inside that

```
Chat bot HTML Template:
        https://themeforest.net/search/chatbot
        https://getbootstrap.com/
```

## To run main script app.py which executes via Flask app:

- Type this in bash

```

python app.py

```

- Once we type, pop will come to run this app in local, just approve it
- Then open this link in explorer, we can see our app running

```
    http://localhost:8080
```

- We can give any Q here and send, it executes backend model and retrives the O/P(Wait for 2 min)

![plot](App_page_image.png)
