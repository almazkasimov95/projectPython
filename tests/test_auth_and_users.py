import requests
import pytest
from models.user import LoginResponse, ErrorResponse, UserListResponse

BASE_URL = "https://reqres.in/api"


def test_successful_login():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)

    assert response.status_code == 200
    data = response.json()

    # Валидация через Pydantic
    login_resp = LoginResponse(**data)
    assert len(login_resp.token) > 0


def test_invalid_password():
    payload = {"email": "eve.holt@reqres.in", "password": "wrong_password"}
    response = requests.post(f"{BASE_URL}/login", json=payload)

    assert response.status_code == 400
    data = response.json()

    # Валидация ошибки
    error_resp = ErrorResponse(**data)
    assert "user not found" in error_resp.error.lower()


def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=1")

    assert response.status_code == 200
    data = response.json()

    # Валидация всей структуры
    users_resp = UserListResponse(**data)

    assert users_resp.page == 1
    assert len(users_resp.data) > 0
    assert users_resp.data[0].email.endswith("@reqres.in")