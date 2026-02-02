# tests/ui/test_login_page.py
import allure
from pages.login_page import LoginPage


@allure.title("Успешный вход в систему")
def test_valid_login(login_page):
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.is_success_message_visible()
    assert "You logged into a secure area!" in login_page.get_success_message_text()


@allure.title("Неверный пароль")
def test_invalid_password(login_page):
    login_page.load()
    login_page.login("tomsmith", "wrongpassword")

    assert login_page.is_error_message_visible()
    assert "Your password is invalid!" in login_page.get_error_message_text()