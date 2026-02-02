# pages/login_page.py

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.success_message = page.locator(".flash.success")

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