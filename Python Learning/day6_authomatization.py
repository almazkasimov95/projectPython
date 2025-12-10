import os
import json
from todo import Task, TaskManager

# Убедимся, что тесты не портят реальные данные
TEST_FILE = "test_tasks.json"

def setup_function():
    """Выполняется перед каждым тестом"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def teardown_function():
    """Выполняется после каждого теста"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_task():
    # Меняем имя файла на тестовый
    manager = TaskManager()
    manager.FILENAME = TEST_FILE

    manager.add_task("Купить молоко")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Купить молоко"
    assert manager.tasks[0].completed == False

def test_complete_task():
    manager = TaskManager()
    manager.FILENAME = TEST_FILE

    manager.add_task("Прогуляться")
    manager.complete_task(1)

    assert manager.tasks[0].completed == True

def test_save_and_load():
    manager = TaskManager()
    manager.FILENAME = TEST_FILE

    manager.add_task("Написать тесты")
    manager.save_tasks()

    # Загружаем заново
    new_manager = TaskManager()
    new_manager.FILENAME = TEST_FILE
    new_manager.load_tasks()

    assert len(new_manager.tasks) == 1
    assert new_manager.tasks[0].title == "Написать тесты"