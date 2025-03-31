from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.analysis import analyze_book
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_index():
    return FileResponse("static/index.html")


@app.get("/book/{book_id}")
def get_book_text(book_id: int):
    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Book not found")
    
    text = response.text
    return JSONResponse(content={"book_id": book_id, "text": text})

@app.get("/analyze/{book_id}")
async def analyze(book_id: int):
    try:
        result = analyze_book(book_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
