from faker import Faker
from playwright.sync_api import Page

from src.web.pages.HomePage import HomePage
from src.web.pages.SignUpPage import SignUpPage
from tests.conftest import Config


def test_signup_invalid(page: Page, configs: Config):
    home_page = HomePage(page)
    home_page.open()
    home_page.is_loaded()
    home_page.click_signup()

    signup_page = SignUpPage(page)
    signup_page.is_loaded()
    signup_page.sign_up(configs.username, configs.invalid_email, Faker().password(length=14, special_chars=False))
    signup_page.invalid_signup_page_visible()
