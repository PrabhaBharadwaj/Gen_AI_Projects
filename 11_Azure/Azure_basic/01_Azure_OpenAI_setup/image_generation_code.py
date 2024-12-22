# Key Authentication

import os
import httpx
from openai import AzureOpenAI
from PIL import Image

from dotenv import load_dotenv

# To load .env from local
load_dotenv()

# Configuration
# Read OPENAI KEY from .env. This key got from AzureopenAPI Resource which we created for GPT4 model

client = AzureOpenAI(
    api_version="2024-02-01",
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
)

result = client.images.generate(
    model="dalle3",  # the name of your DALL-E 3 deployment
    prompt="Create swimming fish in clear water",
    n=1,
)

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, "images")

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, "generated_image.png")

# Retrieve the generated image
image_url = result.data[0].url  # extract image URL from response
generated_image = httpx.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()
print(image_url)
