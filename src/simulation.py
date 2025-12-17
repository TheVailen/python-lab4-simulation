import random
from src.library import Library
from src.entities import Book, PaperBook, EBook
from src.constants import AUTHORS, TITLES, GENRES, FORMATS, COVER_TYPES

def generate_random_book(uid: int) -> Book:
    title = random.choice(TITLES)
    author = random.choice(AUTHORS)
    year = random.randint(1900, 2024)
    genre = random.choice(GENRES)

    part1 = random.randint(0, 9)
    part2 = random.randint(1000, 9999)
    part3 = uid % 10000 
    part4 = random.randint(0, 9)

    isbn = f"978-{part1}-{part2}-{part3:04d}-{part4}"

    if random.choice([True, False]):
        return PaperBook(title, author, year, genre, isbn, 
                         pages=random.randint(100, 900), 
                         cover=random.choice(COVER_TYPES))
    else:
        return EBook(title, author, year, genre, isbn, 
                     file_size_mb=round(random.uniform(0.5, 50.0), 2), 
                     file_format=random.choice(FORMATS))

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
        print(f"--- НАЧАЛО СИМУЛЯЦИИ (SEED: {seed}) ---")
    else:
        print("--- НАЧАЛО СИМУЛЯЦИИ (СЛУЧАЙНЫЙ ЗАПУСК) ---")

    lib = Library()
    book_counter = 0 

    for _ in range(5):
        book_counter += 1
        new_book = generate_random_book(book_counter)
        lib.add_book(new_book)
        print(f"   [INIT] Создана книга: {new_book}")
    print(f"   [INIT] Библиотека предзаполнена. Книг: {len(lib.books)}")


    actions = [
        'add', 
        'remove_random', 
        'search_auth', 
        'search_year', 
        'attempt_get_missing',
        'check_len'
    ] 

    for step in range(1, steps + 1):
        action = random.choice(actions)
        print(f"\nШаг {step:02d} | Действие: ", end="")

        if action == 'add':
            book_counter += 1
            new_book = generate_random_book(book_counter)
            lib.add_book(new_book)
            print(f"ДОБАВЛЕНИЕ: {new_book}")

        elif action == 'remove_random':
            if len(lib.books) > 0:
                idx = random.randint(0, len(lib.books) - 1)
                target = lib.books[idx]
                if lib.remove_book(target):
                    print(f"➖ УДАЛЕНИЕ: '{target.title}' (ISBN: {target.isbn})")
            else:
                print("Удаление невозможно: библиотека уже пуста")

        elif action == 'search_auth':
            auth = random.choice(AUTHORS)
            results = lib.search_author(auth)
            print(f"ПОИСК АВТОРА '{auth}': Найдено {len(results)} шт")
        
        elif action == 'search_year':
            year = random.randint(1900, 2024)
            results = lib.search_year(year)
            print(f"ПОИСК ГОДА {year}: Найдено {len(results)} шт.")

        elif action == 'attempt_get_missing':
            missing_isbn = f"978-{999999999:09d}"
            missing_book = Book("Неизвестный том", "None", 0, "None", missing_isbn)
            if missing_book in lib.books:
                print("Ошибка, книга найдена (не должно случиться)")
            else:
                print(f"ПРОВЕРКА: Книга (ISBN {missing_isbn}) отсутствует (ОК)")

        elif action == 'check_len':
            books_count = len(lib)
            authors_indexed = len(lib.by_author.keys())
            print(f"СТАТУС: Всего книг: {books_count}. Уникальных авторов: {authors_indexed}.")

    print(f"\n--- СИМУЛЯЦИЯ ЗАВЕРШЕНА. Итого книг: {len(lib.books)} ---")