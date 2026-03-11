from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page:  Page):
    page.goto("https://testomat.io")

    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text("Log in", exact=True).click()
    page.locator("#content-desktop #user_email").fill("test@gmail.co")
    page.locator("#content-desktop #user_password").fill("12df34")
    page.get_by_role("button", name="Sign in").click()

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid Email or password.")
    expect(page.locator("#content-desktop").get_by_text("Forgot your password?")).to_be_enabled()

def test_signup_with_invalid_creds(page: Page):
    page.goto("https://testomat.io")

    page.locator(".side-menu .start-item").click()
    page.locator("#content-desktop #user_name").fill("Joe")
    page.locator("#content-desktop #user_email").fill("test@gmail.co")
    page.locator("#content-desktop #user_password").fill("147258369AS@Op")
    page.locator("#content-desktop #user_password_confirmation").fill("147258369AS@O")
    page.locator("#content-desktop #terms").check()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Sign up").click()

    expect(page.locator("#content-desktop .text-red-500")).to_have_text("doesn't match Password")

