# test_button.py
from playwright.sync_api import sync_playwright, expect


def test_button_click():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False — чтобы видеть
        page = browser.new_page()

        # Используем СТАБИЛЬНЫЙ сайт
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # Кликаем по кнопке "Add Element"
        add_button = page.locator("button", has_text="Add Element")
        expect(add_button).to_be_visible()
        add_button.click()

        # Проверяем, что появилась кнопка "Delete"
        delete_button = page.locator("button", has_text="Delete")
        expect(delete_button).to_be_visible()
        assert delete_button.is_visible()

        browser.close()


if __name__ == "__main__":
    test_button_click()