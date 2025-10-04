from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@onclick=\"byCat('monitor')\"]"))
        )
        monitor_link.click()

    def check_product_counts(self, expected_count):  # ← Добавлен параметр
        """
        Проверяет, что количество карточек товаров соответствует ожидаемому.
        :param expected_count: Ожидаемое количество карточек
        """
        # Найдём все карточки товаров. Селектор нужно подобрать правильно!
        product_cards = self.browser.find_elements(By.CSS_SELECTOR, '.card.h-100')  # Пример правильного CSS
        actual_count = len(product_cards)

        assert actual_count == expected_count, \
            f"Ожидалось {expected_count} товаров, найдено {actual_count}"
