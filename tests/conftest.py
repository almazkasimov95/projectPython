# tests/conftest.py
import sys
import os
import pytest
from playwright.sync_api import sync_playwright

# Добавляем корень проекта в PYTHONPATH
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from pages.login_page import LoginPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=True для CI
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com".strip()