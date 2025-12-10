
#Строки: Есть строка " email1@example.com; email2@example.com ".
#Очисти её от пробелов и раздели на список email'ов.
#Файлы: Создай файл notes.txt и запиши в него 3 строки через write(). Затем прочитай и выведи их.
#Исключения + файлы: Напиши программу, которая просит пользователя ввести имя файла, пытается его прочитать и корректно обрабатывает, если файла нет.
#Комбинированная задача:
#Прочитай файл numbers.txt (в нём числа, по одному на строку).
#Посчитай сумму всех чисел и запиши результат в result.txt.


#1 Строки: Есть строка " email1@example.com; email2@example.com ".
# Исходная строка
data = "  email1@example.com; email2@example.com  "

# Очистка от пробелов по краям и разделение по "; "
emails = [email.strip() for email in data.strip().split(";")]
print(emails)
# Вывод: ['email1@example.com', 'email2@example.com']



#2 Очисти её от пробелов и раздели на список email'ов.

# Запись
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Первая заметка\n")
    f.write("Вторая заметка\n")
    f.write("Третья заметка\n")

# Чтение и вывод
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

#3 Файлы: Создай файл notes.txt и запиши в него 3 строки через write(). Затем прочитай и выведи их.

filename = input("Введите имя файла для чтения: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        print("Содержимое файла:")
        print(f.read())
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден.")
except PermissionError:
    print(f"Ошибка: нет прав на чтение файла '{filename}'.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")

#4 Исключения + файлы: Напиши программу, которая просит пользователя ввести имя файла, пытается его прочитать и корректно обрабатывает, если файла нет.

try:
    total = 0
    with open("numbers.txt", "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if line:  # пропускаем пустые строки
                try:
                    total += int(line)
                except ValueError:
                    print(f"Предупреждение: строка {line_number} не является числом: '{line}'")

    # Запись результата
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Сумма чисел: {total}\n")

    print(f"Сумма: {total}. Результат записан в result.txt")

except FileNotFoundError:
    print("Ошибка: файл 'numbers.txt' не найден.")
except Exception as e:
    print(f"Ошибка при обработке: {e}")