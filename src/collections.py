from typing import List, Any, Union, Dict
from src.entities import Book

class BookCollection:
    def __init__(self):
        self._data: List[Book] = []

    def add(self, book: Book):
        self._data.append(book)

    def remove(self, book: Book):
        if book in self._data:
            self._data.remove(book)
        else:
            raise ValueError(f"Книга {book.isbn} не найдена в коллекции")

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: Union[int, slice]) -> Union[Book, List[Book]]:
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
    
    def __contains__(self, item: Book) -> bool:
        return item in self._data


class IndexDict:
    def __init__(self):
        self._index: Dict[Any, List[Book]] = {}

    def add_entry(self, key: Any, book: Book):
        if key not in self._index:
            self._index[key] = []
        self._index[key].append(book)

    def remove_entry(self, key: Any, book: Book):
        if key in self._index:
            try:
                self._index[key].remove(book)
                if not self._index[key]:
                    del self._index[key]
            except ValueError:
                pass 

    def get(self, key: Any) -> List[Book]:
        return self._index.get(key, [])

    def __len__(self) -> int:
        return len(self._index)
    
    def keys(self):
        return self._index.keys()