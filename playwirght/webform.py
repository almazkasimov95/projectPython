from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создание экземпляра веб-драйвера Firefox
browser = webdriver.Firefox()

try:
    # Установка базового URL (без лишних пробелов)
    base_url = 'https://www.saucedemo.com/'
    browser.get(base_url)
    browser.maximize_window()

    # Ожидание загрузки страницы
    time.sleep(2)

    # Ввод логина
    user_name = browser.find_element(By.ID, 'user-name')  # Используем ID вместо XPath — надёжнее
    user_name.send_keys("standard_user")  # Исправлена опечатка

    # Ввод пароля
    password = browser.find_element(By.ID, 'password')
    password.send_keys("secret_sauce")

    # Клик по кнопке
    button_login = browser.find_element(By.ID, 'login-button')
    button_login.click()

    # Ждём результат
    time.sleep(5)

    # (Опционально) Проверка успешного входа — например, наличие элемента на главной странице
    assert "inventory" in browser.current_url, "Login failed!"

finally:
    # Закрываем браузер даже при ошибке
    browser.quit()