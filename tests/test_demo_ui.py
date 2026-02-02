# tests/test_demo_ui.py
from playwright.sync_api import sync_playwright


def test_login_form(page):
   # Стабильный сайт
    page.goto("https://the-internet.herokuapp.com/login")

    # Вводим данные
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    # Проверяем успешный вход
    assert page.is_visible(".flash.success")
    assert "You logged into a secure area!" in page.text_content(".flash")