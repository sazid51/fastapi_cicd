from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Book(BaseModel):
    id: int
    name: str
    description: str
    isAvailable: bool

books: List[Book] = []

@api.get("/")
def index():
    return {"Message": "Welcome to the Book Management System"}

@api.get("/book")
def get_books():
    return books

@api.post("/book")
def add_book(book: Book):
    books.append(book)
    return books

@api.put("/book/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    return {"error": "Book Not Found"}

@api.delete("/book/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return deleted_book
    return {"error": "Book not found, deletion failed"}