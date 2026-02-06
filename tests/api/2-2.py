import requests
import pytest
import allure
from jsonschema import validate

base_url = "https://jsonplaceholder.typicode.com".strip()

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}


@allure.title("Получение поста по ID")
@allure.description("Отправляем GET-запрос к /posts/1 и проверяем структуру ответа")
@allure.feature("POST")
@allure.story("API")
@allure.severity(allure.severity_level.NORMAL)

def test_schema_api():

    url = f"{base_url}/posts/1"

    with allure.step("Отправка GET-запроса"):
        response = requests.get(url)
        assert response.status_code == 200

    with allure.step("Валидация JSON-схемы"):
        json_data = response.json()
        validate(instance=json_data, schema=post_schema)

    with allure.step("Проверка нового userId"):
        assert json_data["userId"] == 1


@allure.title("Создание нового поста")
@allure.description("Отправляем POST-запрос к /posts с данными и проверяем ответ")
@allure.feature("Посты")
@allure.story("API")
@allure.severity(allure.severity_level.CRITICAL)
def test_post():
    post_json = {
        "title": "Тестовый заголовок",
        "body": "Тестовое тело",
        "userId": 1
    }

    url = f"{base_url}/posts"

    with allure.step("Отправка post Запроса"):
        response = requests.post(url, json=post_json)
        assert response.status_code == 201

    with allure.step("Валидация JSON-схемы ответа"):
        json_data = response.json()
        validate(instance=json_data, schema=post_schema)  # ← как в GET-тесте

    with allure.step("Проверка соответствия данных"):
        # проверка на совпадение данных
        assert json_data["title"] == post_json["title"]
        assert json_data["body"] == post_json["body"]
        assert json_data["userId"] == post_json["userId"]
        assert "id" in json_data