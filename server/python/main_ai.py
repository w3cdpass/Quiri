# backend/python/main_ai.py
import os
import requests
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API endpoint
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt: str, model: str = "deepseek/deepseek-r1-0528-qwen3-8b:free", stream: bool = True) -> str:
    """
    Ask the AI a question using OpenRouter.
    If stream=True, prints the response in real time.
    If stream=False, returns the full text as a string.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": stream
    }

    if stream:
        # Streaming mode: print chunks as they arrive
        with requests.post(OPENROUTER_URL, headers=headers, json=payload, stream=True) as r:
            full_text = ""
            for line in r.iter_lines(decode_unicode=True):
                if not line:
                    continue
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        obj = json.loads(data)
                        delta = obj["choices"][0]["delta"].get("content")
                        if delta:
                            print(delta, end="", flush=True)
                            full_text += delta
                    except json.JSONDecodeError:
                        continue
            print()  # newline after streaming
            return full_text
    else:
        # Non-streaming mode: wait for full completion
        res = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        data = res.json()
        return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    while True:
        question = input("\nAsk me something (or 'exit'): ")
        if question.lower() in ["exit", "quit"]:
            break
        ask_ai(question, stream=True)
