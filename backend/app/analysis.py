import requests
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # or use groq.com / sambanova

def fetch_book(book_id: int) -> str:
    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    response = requests.get(url)
    return response.text

def analyze_book(book_id: int):
    text = fetch_book(book_id)[:10000]  # truncate for simplicity
    print(text)
    prompt = f"""
    Extract all characters from this book and identify their interactions.
    Format as:
    {{
      "nodes": [{{"id": "Romeo"}}, {{"id": "Juliet"}}],
      "edges": [{{"source": "Romeo", "target": "Juliet", "weight": 3}}]
    }}
    Book:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
