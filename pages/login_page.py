# pages/login_page.py
from utils.config_loader import load_config

class LoginPage:
    def __init__(self, page, env=None):
        self.page = page
        self.config = load_config(env)
        self.URL = f"{self.config['base_url']}/login"
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.success_message = page.locator(".flash.success")
        self.error_message = page.locator(".flash.error")  # ← добавь эту строку!

    def load(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_success_message_visible(self) -> bool:
        return self.success_message.is_visible()

    def get_success_message_text(self) -> str:
        return self.success_message.text_content()

    # === НОВЫЕ МЕТОДЫ ДЛЯ ОШИБКИ ===
    def is_error_message_visible(self) -> bool:
        return self.error_message.is_visible()

    def get_error_message_text(self) -> str:
        return self.error_message.text_content()

    def login_via_cookie(self, username="tomsmith"):
        # Сначала зайди на страницу, чтобы установить сессию
        self.page.goto(self.URL)
        # Установи cookie напрямую
        self.page.context.add_cookies([{
            "name": "user",
            "value": username,
            "url": self.config["base_url"]
        }])
        # Перезагрузи → должен быть залогинен
        self.page.reload()

    def test_login_via_cookie(login_page):
        login_page.login_via_cookie()
        assert login_page.is_success_message_visible()