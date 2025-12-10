

"""
Модули:
1 Создай программу, которая генерирует случайную дату в 2025 году и выводит, какой это день недели.
(Подсказка: используй random.randint() + datetime + .strftime("%A"))
List comprehensions:
2 Дан список: words = ["python", "java", "c++", "go"].
Создай новый список, содержащий только те слова, длина которых > 3, в верхнем регистре.
ООП:
3 Создай класс Book с атрибутами title, author, pages.
Добавь метод is_long(), который возвращает True, если страниц > 300.
Создай 2 книги и проверь.
Комбинированная задача:
4 Используй random и datetime, чтобы создать список из 5 случайных дат в декабре 2025.
Отсортируй их с помощью list comprehension + sorted().
"""



# Задача 1. Модули: случайная дата в 2025 году → день недели

import random
from datetime import datetime, timedelta

# Генерируем случайный день в 2025 году
# 2025 не является високосным → 365 дней
random_day = random.randint(1, 365)

# Начало года
start_of_year = datetime(2025, 1, 1)

# Добавляем случайное количество дней
random_date = start_of_year + timedelta(days=random_day - 1)

# Выводим дату и день недели
print(f"Случайная дата: {random_date.strftime('%Y-%m-%d')}")
print(f"День недели: {random_date.strftime('%A')}")



# Задача 2. List comprehensions: фильтрация и преобразование

words = ["python", "java", "c++", "go"]

# Только слова длиной > 3, в верхнем регистре
long_words_upper = [word.upper() for word in words if len(word) > 3]

print(long_words_upper)  # ['PYTHON', 'JAVA']




# Задача 3. ООП: класс Book

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

# Создаём две книги
book1 = Book("Война и мир", "Л. Толстой", 1225)
book2 = Book("Маленький принц", "А. де Сент-Экзюпери", 96)

# Проверяем
print(f"'{book1.title}' длинная? {book1.is_long()}")  # True
print(f"'{book2.title}' длинная? {book2.is_long()}")  # False




# Задача 4. Комбинированная: 5 случайных дат в декабре 2025 → сортировка

import random
from datetime import datetime

# Генерируем 5 случайных дат в декабре 2025 (дни с 1 по 31)
random_dates = []
for _ in range(5):
    day = random.randint(1, 31)
    try:
        date = datetime(2025, 12, day)
        random_dates.append(date)
    except ValueError:
        # На случай, если будет 31 февраля (но в декабре 31 день, так что не случится)
        pass

# Сортируем даты (можно без list comprehension — sorted() возвращает новый список)
sorted_dates = sorted(random_dates)

# Выводим красиво
for d in sorted_dates:
    print(d.strftime("%d.%m.%Y"))