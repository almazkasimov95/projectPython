import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, completed=False, created_at=None):
        self.title = title
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            completed=data["completed"],
            created_at=data["created_at"]
        )

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title}"


class TaskManager:
    FILENAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Задача '{title}' добавлена.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True
            print(f"Задача '{self.tasks[index - 1].title}' отмечена как выполненная.")
        else:
            print("Неверный номер задачи.")

    def save_tasks(self):
        with open(self.FILENAME, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=2)

    def load_tasks(self):
        if not os.path.exists(self.FILENAME):
            return
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Ошибка при загрузке задач: {e}. Файл повреждён или пуст.")
            self.tasks = []

    def run(self):
        while True:
            print("\n--- Менеджер задач ---")
            print("1. Показать задачи")
            print("2. Добавить задачу")
            print("3. Отметить как выполненную")
            print("4. Выйти")
            choice = input("Выберите действие (1-4): ")

            if choice == "1":
                self.list_tasks()
            elif choice == "2":
                title = input("Введите название задачи: ").strip()
                if title:
                    self.add_task(title)
                    self.save_tasks()
                else:
                    print("Название не может быть пустым.")
            elif choice == "3":
                self.list_tasks()
                if self.tasks:
                    try:
                        num = int(input("Введите номер задачи для завершения: "))
                        self.complete_task(num)
                        self.save_tasks()
                    except ValueError:
                        print("Пожалуйста, введите число.")
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    app = TaskManager()
    app.run()