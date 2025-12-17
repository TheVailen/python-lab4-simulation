import pytest
from src.entities import Book, PaperBook, EBook
from src.collections import BookCollection, IndexDict
from src.library import Library
from src.simulation import generate_random_book


@pytest.fixture
def sample_paper():
    return PaperBook("Война и Мир", "Лев Толстой", 1869, "Классика", "ISBN-001", 1225, "Твердая")

@pytest.fixture
def sample_ebook():
    return EBook("1984", "Джордж Оруэлл", 1949, "Антиутопия", "ISBN-002", 1.5, "EPUB")

@pytest.fixture
def lib():
    return Library()

def test_book_equality(sample_paper):
    same_isbn_book = Book("Другое название", "Другой автор", 2000, "Жанр", "ISBN-001")
    assert sample_paper == same_isbn_book

def test_repr_methods(sample_paper, sample_ebook):
    assert "Лев Толстой" in repr(sample_paper)
    assert "[E-Book]" in repr(sample_ebook)

def test_book_collection_magic(sample_paper, sample_ebook):
    col = BookCollection()
    col.add(sample_paper)
    col.add(sample_ebook)

    assert len(col) == 2               
    assert col[0] == sample_paper      
    assert sample_ebook in col          
    
    titles = [b.title for b in col]
    assert "1984" in titles

def test_index_dict_logic(sample_paper):
    idx = IndexDict()
    idx.add_entry("Лев Толстой", sample_paper)
    
    assert len(idx) == 1
    assert "Лев Толстой" in idx.keys()
    assert idx.get("Лев Толстой")[0] == sample_paper
    
    idx.remove_entry("Лев Толстой", sample_paper)
    assert len(idx) == 0

def test_library_integration(lib, sample_paper, sample_ebook):
    lib.add_book(sample_paper)
    lib.add_book(sample_ebook)
    
    results = lib.search_author("Лев Толстой")
    assert len(results) == 1
    assert results[0].title == "Война и Мир"

    lib.remove_book(sample_paper)
    assert len(lib) == 1
    assert len(lib.search_author("Лев Толстой")) == 0

def test_generator():
    book = generate_random_book(uid=1)
    assert isinstance(book, (PaperBook, EBook))
    assert book.isbn.startswith("978-")
    assert "0001" in book.isbn
