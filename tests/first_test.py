import re

from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page:  Page):
    open_home_page(page)

    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text("Log in", exact=True).click()
    login_user(page,"dm.sv.qt@gmail.com", "2578#341")

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid Email or password.")
    expect(page.locator("#content-desktop").get_by_text("Forgot your password?")).to_be_enabled()

def test_signup_with_invalid_creds(page: Page):
    open_home_page(page)
    sign_up(page, "Joe", "test@gmail.co", "1472583")

    expect(page.locator("#content-desktop .text-red-500")).to_have_text(re.compile("^ must contain at least"))

def test_search_project_in_company(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page,"dm.sv.qt@gmail.com", "2578#341As90KL")
    target_project = "Course PW Python"
    search_for_project(page, target_project)

    expect(page.get_by_role("heading", name=target_project)).to_be_visible()

def test_should_be_possible_to_open_free_project(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page,"dm.sv.qt@gmail.com", "2578#341As90KL")
    select_free_project(page)
    target_project = "Course PW Python"
    search_for_project(page, target_project)

    expect(page.get_by_role("heading", name=target_project)).to_be_hidden()
    expect(page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=6000)

def test_button_free_plan_should_be_visible(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page,"dm.sv.qt@gmail.com", "2578#341As90KL")

    expect(page.locator("#content-desktop .tooltip-project-plan")).to_be_visible()

def test_link_read_docs_is_enabled(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page,"dm.sv.qt@gmail.com", "2578#341As90KL")
    select_free_project(page)

    expect(page.locator("[href='https://docs.testomat.io'].underline")).to_be_enabled()


def open_home_page(page: Page):
    page.goto("https://testomat.io")

def sign_up(page: Page, name: str, email: str, password: str):
    page.locator(".side-menu .start-item").click()
    page.locator("#content-desktop #user_name").fill(name)
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.locator("#content-desktop #user_password_confirmation").fill(password)
    page.locator("#content-desktop #terms").check()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Sign up").click()

def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()

def search_for_project(page: Page, target_project: str):
    page.locator("#content-desktop #search").fill(target_project)

def select_free_project(page: Page):
    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")

