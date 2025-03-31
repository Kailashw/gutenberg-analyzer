from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.analysis import analyze_book
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

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

@app.get("/analyze/{book_id}")
async def analyze(book_id: int):
    try:
        result = analyze_book(book_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
