# Key Authentication

import os
import requests
import base64
from dotenv import load_dotenv

# To load .env from local
load_dotenv()

# Configuration
# Read OPENAI KEY from .env. This key got from AzureopenAPI Resource which we created for GPT4 model
API_KEY = os.environ.get("azure_openapi_gpt4_key")
# API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxx"


# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are Insurance assistance. Please provide details related to that. Provide info with soft manner",
                }
            ],
        },
        {"role": "user", "content": [{"type": "text", "text": "Hi who are you?"}]},
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Hello! I'm here to assist you with any insurance-related inquiries you might have. How can I help you today? 😊",
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What are different health insurance"}
            ],
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Health insurance comes in various forms to suit different needs and preferences. Here are some common types of health insurance plans:\n\n1. **Health Maintenance Organization (HMO)**: This plan requires you to select a primary care physician and get referrals from them to see specialists. It typically offers lower premiums and minimal paperwork.\n\n2. **Preferred Provider Organization (PPO)**: PPO plans provide more flexibility in choosing healthcare providers. You don’t need referrals for specialists, but using doctors within the network saves you money.\n\n3. **Exclusive Provider Organization (EPO)**: An EPO plan is a mix between HMO and PPO plans. You don’t need referrals for specialists, but you must stick to the plan’s network except in emergencies.\n\n4. **Point of Service (POS)**: This plan is a combination of HMO and PPO features. You choose a primary care physician, but you can also see out-of-network providers, usually at a higher cost.\n\n5. **High Deductible Health Plan (HDHP)**: Often paired with Health Savings Accounts (HSAs), these plans have higher deductibles but lower premiums. They’re suitable if you’re generally healthy and want to save for potential medical expenses.\n\n6. **Catastrophic Health Insurance**: Designed for people under 30 or those who qualify for a hardship exemption. These plans have very high deductibles and primarily protect you from worst-case scenarios.\n\nEach type of plan offers different levels of coverage, cost-sharing, and flexibility. It's essential to consider your health needs, financial situation, and preferences when choosing a plan. If you need more detailed guidance or have specific conditions to consider, feel free to ask. I'm here to help! 😊",
                }
            ],
        },
        # When I execute this in cmd - 'python chat_completion_code.py'. It gives answer
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What are insurance company in singapore"}
            ],
        },
    ],
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 800,
}

# This is the endpoint for newly deployed GPT4 Model in my AzureopenAI subscription
ENDPOINT = "https://livegenaiclass.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())
