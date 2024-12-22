import requests
import json
import gradio as gr

##Copy URL From OLLAMA githun page. https://github.com/ollama/ollama
"""REST API
Ollama has a REST API for running and managing models.

Generate a response
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}'
"""

# Define URL and header
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

history = []


def generate_response(prompt):
    history.append(prompt)

    final_prompt = "\n".join(history)

    data = {"model": "llama2", "prompt": "final_prompt", "stream": False}

    # Call Ollama from url api
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data["response"]
        return actual_response
    else:
        print("Error", response.text)


# Write Gradio interface code
## Here we are creating gradio interface/UI
interface = gr.Interface(
    fn=generate_response,  # mention function name to be executed
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt"),  # Define input UI part
    outputs="text",  # Define output data format
)

# Execute/launch gradio
interface.launch()


# Execute "python test.py" in cmd to run this notebook
