from  openai import OpenAI
import os
from config.settings import load_env
    
import requests
import requests
import json

def call_deepseek_api(command:str):
    load_env()
    api_key = os.getenv("OPEN_ROUTER_KEY")  # Replace with your actual API key

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Replace if needed
        "X-Title": "Purushu",  # Replace if needed
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises exception for HTTP errors
        result = response.json()
        print(result)
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return f"Unexpected response format: {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example call


    # print(result["choices"][0]["message"]["content"])
