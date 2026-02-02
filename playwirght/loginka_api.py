from playwright.sync_api import sync_playwright, expect
import requests
import pytest

base_url = "https://the-internet.herokuapp.com/api


#проверка, что всё проходит хорошо

def test_success_login():
    payload = {
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
    }
    response = requests.post(f"{base_url}/login", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert len(data["token"]) > 0

#проверка, что приходит 401 не авторизован

def test_failure_login():
    payload = {
        "username": "tomsmith",
        "password": "SuperSecretPassword1!",
    }
    response = requests.post(f"{base_url}/login", json=payload)

    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"


def test_access_secure_endpoint_with_token():
    login_response = requests.post(f"{base_url}/login", json={
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
    })
    token = login_response.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}
    secure_resp = requests.post(f"{base_url}/login", headers=headers)
    assert secure_resp.status_code == 200
    assert "Welcome" in secure_resp.json()["message1"]

def test_access_secure_without_token():
    response = requests.get(f"{base_url}/secure")
    assert response.status_code == 401