from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


try:
    browser = webdriver.Firefox()
    browser.get('https://www.saucedemo.com')
    browser.maximize_window()
    assert browser.current_url == "https://www.saucedemo.com/"

    time.sleep(2)

    user_name = browser.find_element(By.ID, 'user-name')
    user_name.clear()
    user_name.send_keys("standard_user")
    time.sleep(2)

    password = browser.find_element(By.ID, 'password')
    password.clear()
    password.send_keys("secret_sauce")
    time.sleep(2)

    button_login = browser.find_element(By.ID, 'login-button')
    button_login.click()
    time.sleep(2)

    assert "inventory" in browser.current_url, "login failed"

    add_to_backet = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_to_backet.click()
    time.sleep(2)


    check_backet = browser.find_element(By.ID, 'shopping_cart_container')
    check_backet.click()
    time.sleep(5)

    # remove_from_backet=browser.find_element(By.ID, 'remove-sauce-labs-bike-light')
    # remove_from_backet.click()
    # time.sleep(2)

    item_name_to_check = "Sauce Labs Bike Light"
    try:
        # Пытаемся найти элемент с названием товара
        item_element = browser.find_element(By.XPATH,
                                            f"//div[@class='cart_item']//div[contains(text(), '{item_name_to_check}')]")
        # Если элемент найден, значит товар ВСЁ ЕЩЁ в корзине -> тест не пройдён
        assert False, f"Товар '{item_name_to_check}' всё ещё присутствует в корзине!"
    except NoSuchElementException:
        # Если элемент не найден, это ожидаемое поведение -> товар успешно удалён
        print(f"Товар '{item_name_to_check}' успешно удалён из корзины.")

    # try:
    #     backet_items = browser.find_elements(By.CLASS_NAME, 'cart_item')
    #     assert len(backet_items)==0,  f"В корзине всё ещё находятся товары: {len(backet_items)}"
    #     print("Корзина пуста")
    # except AssertionError as e:
    #     print(e)

finally:
   browser.quit()