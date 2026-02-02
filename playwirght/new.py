
"""
# день 1

#Типы данных

# Целое число

age1 = 29 # int

# Число с плавающей точкой

temperature = 36.6 # float

# Строка

name1 = "Алмаз" # str

# Логическое значение

is_worker = True # bool всегда True или False, с большой буквы!


# Переменные операции
a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333всегда float!
print(a // b) # 3 целочисленное значение
print(a % b) # 1 остаток от деления
print(a ** b) # 1000 возведение в степень
"""

#Ввод\вывод

#print("Привет, мир!")

#name = input("Как тебя зовут?")
#print("Привет, " +name + "!")


#age = int(input("Сколько тебе лет? "))
#print(age)

# Условия

#Сравнения: ==, !=, <, >, <=, >=
#Логические операторы: and, or, not
"""
age = int(input("Ваш возраст: "))
if age >= 18 and age <= 60:
    print("Вы совершеннолетний")
elif age < 18:
    print("Пиво не купишь")
else:
    print("Дед уже")
"""

"""
# Базовые структуры данных
#Список(list) - изменяемый упорядоченный

fruits = ["banana", "orange", "peenaple"]
fruits.append("apple") # добавить яблоко
print(fruits[3]) # покажет что добавлено яблоко

#кортеж(tuple) неизменяемый
point = (3, 5)
print(point[1]) # 5
#point[0] = 100 ошибка будет нельзя менять


"""
#Словарь(dict) — пары
"ключ: значение"
"""
person = {"name": "Радмир", "age": 18}
print(person["name"]) # Радмир
person["city"] = "Казань"
for person in person.values():
    print(person)
    """

"""
# Множество (set) — уникальные элементы, без порядка
colors = {"красный", "зеленый", "синий"}
colors.add("желтый")
print("красный" in colors) """


"""
Задачи на практику 


print("Введите два числа")
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 > num2:
    print(num1)
else:
    print(num2)
"""

"""
names = ["Алмаз", "Айгуль", "Радель"]
print(names[1])
"""

"""
car = {"brand": "Toyota", "model": "Camry", "year": "2020"}
print("Я езжу на " + car["brand"] + " " + car["model"] + " " + car["year"] + " " +"года")
"""
"""
name = input("Ваше имя: ")
age = int(input("Сколько лет? "))
print("Привет, " + name + "!  " + "Через 10 лет тебе будет " + (age+10) "лет ")
"""

# День 2

# Циклы
#for
# пример 1: перебор чисел
"""
for i in range(5): # 0, 1, 2, 3, 4
    print(i)
    print("odin")

for i in range(3,8):
    print(i)
    print("dva")

for i in range(0,10,2):
    print(i)
    print("tri")

# пример 2: перебор списка
fruits = ["banana", "orange", "peenaple"]
for fruit in fruits:
    print(f"Я люблю {fruit}!")
"""
#while
"""
count = 0
while count < 5:
    print("Повтор №", count+1)
    count += 1
"""

#break + continue
#break — немедленно выйти из цикла.
#continue — перейти к следующей итерации (пропустить остаток тела цикла).

"""
for i in range(1,6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
"""

# def - функция, которую можно вызвать несколько раз
 # простая функция без параметров
"""
def greet():
    print("Привет! Добро пожаловать!")

greet() # вызов

# функция с параметрами
def greet_user(name, age ):
    print(f"Привет, {name}! Тебе {age} лет.")

greet_user("Алмаз", 29)

# функция возвращающая значение(return)

def square(x):
    return x * x

result = square(5)
print(result) # 25
"""


# области видимости
#Локальные переменные — внутри функции. Доступны только внутри.
#Глобальные переменные — вне функций. Доступны везде, но менять их внутри функции без global нельзя.
"""
name = "Глобальный Алмаз" # глобальная переменная

def my_func():
    name = "Локальный боб" # локальная, не меняет глобальную
    print(name)

my_func() # Локальный боб
print(name) # Глобальный Алмаз
"""



# День 3

# Строковые методы
# split - разбить строку на список
"""
text = "яблоко, банан, дыня"
split_text = text.split(", ")
print(split_text)
"""

# join - собрать список в строку
"""
words = ["Привет", "меня", "зовут", "Алмаз"]
string = " ".join(words)
print(string)
"""

# strip - убрать пробелы по краям
#Есть lstrip() (слева) и rstrip() (справа).
"""
user_input = "   almaz@mail.ru  \n"
clean = user_input.strip()
print("Было:",user_input)
print("Стало:",clean)
"""

# replace - заменить подстроку
"""
text = "Привет, Айгуль!"
greeting = text.replace("Айгуль", "Алмаз")
print(greeting)
"""

# форматирование f-strings
"""
name = "Алмаз"
age = 29
message = f"Привет, {name}! Тебе через 10 лет будет {age + 10 } лет !"
print(message)
"""

# чтение и запись файлов
#запись
"""
with open("log1.txt", "w", encoding="utf-8") as f:
    f.write("Пользователь вошел в систему \n")
#чтение по строкам
with open("log1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
"""


# обработка исключений try\except
"""
try:
    with open("log.txt", "w", encoding="utf-8") as f:
        data = f.write("q")
except FileNotFoundError:
    print("Файл не найден! Проверьте путь")
except PermissionError:
    print("Не хватает прав на чтение !")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
"""

# обработка ошибок при конвертации
"""
try:
    age = int(input("Ваш возраст: "))
    print(age)
except ValueError:
    print("Пожалуйста, введите число")
"""



# День 4

#Импорт модулей: import

#math — математика
"""
import math

print(math.sqrt(16))
print(math.factorial(16))
print(math.ceil(3.14))
print(math.pi)
"""

#random — случайные значения
"""
import random 

print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))
"""

#datetime — работа с датой и временем
"""
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # 2025-12-10 14:30

# Создать свою дату
birthday = datetime(1990, 5, 15)
print(birthday.year)  # 1990
"""

# List comprehensions — списковые включения
# [выражение for элемент in последовательность if условие]

"""
# Обычный способ
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# С фильтрацией
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Строки
names = ["алиса", "БОБ", "Вика"]
cap_names = [name.capitalize() for name in names]  # ['Алиса', 'Боб', 'Вика']
"""



# Основы ООП: КЛассы и объекты
"""
class Dog:
    def __init__(self, name, breed): # __init__ конструктор
        self.name = name #self - ссылка на текущий объект
        self.breed = breed

    def bark(self):
        return f"{self.name} говорит: Гав!"

# Создаем объекты
dog1 = Dog("Рекс", "Овчарка")
dog2 = Dog("Луна", "Хаски")

print(dog1.bark())
print(dog2.bark())
"""

"""
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount}. Баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        elif amount <= 0:
            print("Сумма должна быть положительной.")
        else:
            self.balance -= amount
            print(f"Снятие: -{amount}. Баланс: {self.balance}")

# Использование
account = BankAccount("Алиса", 1000)
account.deposit(500)
account.withdraw(200)
"""



z = 10

def test(x = 5):
    print(x)
    print(z)
    z = 13

test(7)
print(z)