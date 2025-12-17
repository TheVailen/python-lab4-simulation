from typing import List
from src.entities import Book
from src.collections import BookCollection, IndexDict

class Library:
    def __init__(self):
        self.books = BookCollection()
        
        self.by_author = IndexDict()
        self.by_year = IndexDict()
        self.by_isbn = IndexDict()

    def add_book(self, book: Book):
        self.books.add(book)
        self.by_author.add_entry(book.author, book)
        self.by_year.add_entry(book.year, book)
        self.by_isbn.add_entry(book.isbn, book)

    def remove_book(self, book: Book):
        try:
            self.books.remove(book)
            self.by_author.remove_entry(book.author, book)
            self.by_year.remove_entry(book.year, book)
            self.by_isbn.remove_entry(book.isbn, book)
            return True
        except ValueError:
            return False

    def search_author(self, author: str) -> List[Book]:
        return self.by_author.get(author)

    def search_year(self, year: int) -> List[Book]:
        return self.by_year.get(year)

    def __len__(self):
        return len(self.books)