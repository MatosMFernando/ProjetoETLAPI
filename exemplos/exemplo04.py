import requests
import json
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()


url = "https://api.openai.com/v1/chat/completions"

openai_api_key = os.getenv("OPEN_AI_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)