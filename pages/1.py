from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.success_message = page.locator("h2")
        self.error_message = page.locator(".flash.error")

    def load(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_success_message_visible(self) -> bool:
        return self.success_message.is_visible()

    def get_success_text(self) -> str:
        return self.success_message.text_content()

    def is_error_message_visible(self) -> bool:
        return self.error_message.is_visible()

    def get_error_text(self) -> str:
        return self.error_message.text_content()
class LoginPage2(Page):
    def base_url_2(self) -> str:
        return "https://jsonplaceholder.typicode.com/posts/"