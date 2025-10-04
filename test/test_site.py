import pytest
import value
from docutils.nodes import title
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pages.homepage import HomePage
from pages.product import ProductPage




def test_open_s6(browser):
    options = Options()
    options.add_argument('--headless')
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)  # Лучше заменить на явное ожидание
    homepage.check_product_counts(2)  # Теперь всё ок: 2 передаётся как expected_count