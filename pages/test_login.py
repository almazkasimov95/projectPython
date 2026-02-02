# tests/test_login.py
import allure
from pages.login_page import LoginPage

@allure.title("Успешный вход в систему")
@allure.description("Вводим валидные креды -> видим success message")
def test_login_success(page):
    with allure.step("Загружаем страницу логина"):
        login_page = LoginPage(page)
        login_page.load()

    with allure.step("Выполняем вход"):
        login_page.login("tomsmith", "SuperSecretPassword!")

    with allure.step("Проверяем сообщение об успехе"):
        assert login_page.is_success_message_visible()
        assert "You logged into a secure area!" in login_page.get_success_message_text()