from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.clear()
    email_input.fill('user.name@gmail.com')
    page.wait_for_timeout(2000)

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.clear()
    password_input.fill('Password')

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).not_to_be_disabled()

    page.wait_for_timeout(5000)