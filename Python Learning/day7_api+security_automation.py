import requests
import pytest

BASE_URL = "https://httpbin.org"

# Валидный токен (httpbin принимает любой непустой)
VALID_TOKEN = "abc123xyz"
INVALID_TOKEN = "invalid_token"
OTHER_USER_TOKEN = "another_user_token"


def test_valid_token_returns_200():
    """Позитивный сценарий: валидный токен → 200"""
    headers = {"Authorization": f"Bearer {VALID_TOKEN}"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)
    assert response.status_code == 200
    assert response.json()["token"] == VALID_TOKEN


def test_missing_token_returns_401():
    """Нет токена → 401 Unauthorized"""
    response = requests.get(f"{BASE_URL}/bearer")
    assert response.status_code == 401


def test_invalid_token_returns_401():
    """Невалидный/битый токен → 401"""
    headers = {"Authorization": f"Bearer {INVALID_TOKEN}"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)
    assert response.status_code == 401


def test_token_substitution_returns_403():
    """
    Подмена токена (даже валидного, но чужого) → 403 Forbidden
    В реальной системе это критично!
    """
    # Эмулируем: у нас токен другого пользователя
    headers = {"Authorization": f"Bearer {OTHER_USER_TOKEN}"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)

    # ⚠️ httpbin не различает пользователей, поэтому он вернёт 200.
    # В НАСТОЯЩЕЙ СИСТЕМЕ здесь должен быть 403!
    # Но мы всё равно пишем тест — он "упадёт", если система уязвима.
    assert response.status_code == 403, "Уязвимость: система не проверяет ownership токена!"


def test_sql_injection_in_token():
    """Проверка на SQL-инъекцию через токен"""
    malicious_token = "'; DROP TABLE users; --"
    headers = {"Authorization": f"Bearer {malicious_token}"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)

    # Ожидаем: либо 401 (недопустимый токен), либо 200 с экранированным токеном
    # Но НЕ должен быть 500 (ошибка сервера) — это признак уязвимости!
    assert response.status_code != 500, "Возможна SQL-инъекция!"
    # Дополнительно: можно проверить, что токен не исполняется как SQL


def test_xss_in_token():
    """Проверка на XSS через токен (если токен отображается в UI/API)"""
    xss_token = "<script>alert('xss')</script>"
    headers = {"Authorization": f"Bearer {xss_token}"}
    response = requests.get(f"{BASE_URL}/bearer", headers=headers)

    # Токен должен быть экранирован или отклонён
    assert "<script>" not in response.text, "Возможна XSS-уязвимость!"