import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
