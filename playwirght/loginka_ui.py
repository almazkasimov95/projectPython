# test_login.py
from playwright.sync_api import expect
import pytest


def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


def test_invalid_username(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "wronguser")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")


def test_invalid_password(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "wrongpass")
    page.click("button[type='submit']")

    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")


def test_logout(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    page.click("text=Logout")
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")