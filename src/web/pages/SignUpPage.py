from playwright.sync_api import Page, expect


class SignUpPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("/users/sign_up")

    def is_loaded(self):
        expect(self.page.locator("#content-desktop #new_user")).to_be_visible()

    def sign_up(self, name: str, email: str, password: str):
        self.page.locator("#content-desktop #user_name").fill(name)
        self.page.locator("#content-desktop #user_email").fill(email)
        self.page.locator("#content-desktop #user_password").fill(password)
        self.page.locator("#content-desktop #user_password_confirmation").fill(password)
        self.page.locator("#content-desktop #terms").check()
        self.page.wait_for_timeout(6000)
        self.page.get_by_role("button", name="Sign up").click()

    def invalid_signup_page_visible(self):
        expect(self.page.locator("#content-desktop .text-red-500")).to_contain_text("must contain special")
