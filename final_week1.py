# final_week1.py
import json
import os
from utils.user_utils import check_age  # ← импортируем функцию


def save_user_data(name: str, age: int, folder: str = "data") -> None:
    """Сохраняет данные пользователя в JSON-файл."""
    os.makedirs(folder, exist_ok=True)
    data = {"name": name, "age": age}
    filepath = os.path.join(folder, f"{name}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    try:
        name = input("Введите ваше имя: ").strip()
        if not name:
            print("Имя не может быть пустым!")
            return

        age_input = input("Введите ваш возраст: ").strip()
        age = int(age_input)

        if age < 0:
            print("Возраст не может быть отрицательным!")
            return

        # Используем функцию из user_utils.py
        message = check_age(age)
        print(message)

        save_user_data(name, age)
        print(f"Данные сохранены в data/{name}.json")

    except ValueError:
        print("Ошибка: возраст должен быть числом!")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()