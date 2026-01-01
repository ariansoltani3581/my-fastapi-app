from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

books = [
    {"id": 1, "title": "Python Basics", "author": "Real P", "pages": "635"},
    {"id": 2, "title": "Breaking The Rules", "author": "Stephen G.", "pages": "99"},
]

class Book(BaseModel):
    title: str
    author: str
    pages: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }
    books.append(new_book)
    return new_book