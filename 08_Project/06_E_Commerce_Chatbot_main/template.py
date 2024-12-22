import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

# Normally kepts inside src folder instead of ecommbot
list_of_files = [
    "ecommbot/__init__.py",
    "ecommbot/data_converter.py",
    "ecommbot/ingest.py",
    "templates/ingest.py",
    "data/test.py",
    ".env",
    ".gitignore",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "test.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the files {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")
