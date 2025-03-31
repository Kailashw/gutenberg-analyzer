import os
import requests
from groq import Groq  # ✅ Groq SDK
from fastapi import HTTPException
import json
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # ✅ Use Groq key

def fetch_book(book_id: int) -> str:
    base_url = f"https://www.gutenberg.org/files/{book_id}/"
    possible_suffixes = [
        f"{book_id}-0.txt",
        f"{book_id}.txt",
        f"{book_id}.txt.utf-8",
        f"{book_id}-8.txt",
        f"{book_id}-0.txt.utf-8",
    ]

    print("API_Key:", os.getenv("GROQ_API_KEY"))  # ✅ Debugging line
    for suffix in possible_suffixes:
        url = base_url + suffix
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    raise HTTPException(status_code=404, detail="Book text not found")

import json
from groq import Groq
from fastapi import HTTPException

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_book(book_id: int):
    text = fetch_book(book_id)[:10000]  # Truncate if large

    system_message = {
        "role": "system",
        "content": (
            "You are a helpful assistant. Your task is to extract all characters from a book "
            "and identify their interactions. Respond strictly in a JSON object with the following structure:\n\n"
            "{\n"
            '  "nodes": [{"id": "Character1"}, {"id": "Character2"}],\n'
            '  "edges": [{"source": "Character1", "target": "Character2", "weight": 2}]\n'
            "}\n\n"
            "Do not include any explanation or markdown formatting like ```json."
        )
    }

    user_message = {
        "role": "user",
        "content": f"Analyze the following book excerpt:\n{text}"
    }

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[system_message, user_message],
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        response_text = response.choices[0].message.content.strip()
        print("Raw LLM Response:", response_text)

        parsed = json.loads(response_text)
        print("Parsed JSON:", parsed)
        return parsed

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        raise HTTPException(status_code=500, detail="LLM did not return valid JSON")

    except Exception as e:
        print("GROQ LLM error:", e)
        raise HTTPException(status_code=500, detail="LLM analysis failed")


    
    