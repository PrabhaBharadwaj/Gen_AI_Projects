from fastapi import (
    FastAPI,
    Form,
    Request,
    Response,
    File,
    Depends,
    HTTPException,
    status,
)
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import aiofiles
import json
import csv
from src.helper import (
    llm_pipeline,
)  # Here this func O/P's ans generation chain AND list of Q


# Initialize FastAPI
app = FastAPI()

# It points to static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Point template design which written in templates folder index.html
templates = Jinja2Templates(directory="templates")


# Run code, so it executes in local host
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# During Upload file
@app.post("/upload")
async def chat(request: Request, pdf_file: bytes = File(), filename: str = Form(...)):
    base_folder = "static/docs/"  # It saves I/P files in this folder
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    pdf_filename = os.path.join(base_folder, filename)

    async with aiofiles.open(pdf_filename, "wb") as f:
        await f.write(pdf_file)

    response_data = jsonable_encoder(
        json.dumps({"msg": "success", "pdf_filename": pdf_filename})
    )
    res = Response(response_data)
    return res


# In this function, it reads file from static/docs/ and calls llm_pipeline to generate Q+A pair
def get_csv(file_path):
    # Here based on I/P file, it O/P ans generation chain AND list of Q
    answer_generation_chain, ques_list = llm_pipeline(file_path)
    base_folder = "static/output/"
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    output_file = base_folder + "QA.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Question", "Answer"])  # Writing the header row

        # Call ans generation chain one by one for each Q
        for question in ques_list:
            print("Question: ", question)
            answer = answer_generation_chain.run(question)
            print("Answer: ", answer)
            print("--------------------------------------------------\n\n")

            # Save answer to CSV file
            csv_writer.writerow([question, answer])
    return output_file


# When user clicks Generate Q&A button, this triggers this analyze
# and generates Q+A csv by calling get_csv function
@app.post("/analyze")
async def chat(request: Request, pdf_filename: str = Form(...)):
    # Here it calls main func get_csv where RAG process happens
    output_file = get_csv(pdf_filename)
    response_data = jsonable_encoder(json.dumps({"output_file": output_file}))
    res = Response(response_data)
    return res


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
    # Here port no set to 8000
