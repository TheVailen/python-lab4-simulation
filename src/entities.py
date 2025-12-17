from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    isbn: str

    def __repr__(self) -> str:
        return f"'{self.title}' ({self.author}, {self.year}) [{self.genre}]"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn

@dataclass
class PaperBook(Book):
    pages: int = 0
    cover: str = "Твердая"

    def __repr__(self) -> str:
        return f"[Paper] {super().__repr__()} - {self.pages} стр."

@dataclass
class EBook(Book):
    file_size_mb: float = 0.0
    file_format: str = "PDF"

    def __repr__(self) -> str:
        return f"[E-Book] {super().__repr__()} - {self.file_size_mb} MB"