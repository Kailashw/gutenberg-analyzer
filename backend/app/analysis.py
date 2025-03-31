import requests
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # or use groq.com / sambanova

def fetch_book(book_id: int):
    base_url = f"https://www.gutenberg.org/files/{book_id}/"
    possible_suffixes = [
        f"{book_id}-0.txt",
        f"{book_id}.txt",
        f"{book_id}.txt.utf-8",
        f"{book_id}-8.txt",
        f"{book_id}-0.txt.utf-8",
    ]

    for suffix in possible_suffixes:
        url = base_url + suffix
        response = requests.get(url)
        print(f"Trying URL: {url}")
        if response.status_code == 200:
            print(response.text)
        if response.status_code == 200:
            return JSONResponse(content={"book_id": book_id, "text": response.text})

    raise HTTPException(status_code=404, detail="Book text not found in any known format")


def analyze_book(book_id: int):
    text = fetch_book(book_id)[:10000]  # truncate for simplicity
    print(text)
    return {"status": "success", "data": text}
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
