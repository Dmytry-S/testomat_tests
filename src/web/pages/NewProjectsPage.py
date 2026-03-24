from playwright.sync_api import expect, Page


class NewProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self.form_container = page.locator("#content-desktop [action='/projects']")

    def open(self):
        self.page.goto("/projects/new")

    def is_loaded(self):
        expect(self.form_container).to_be_visible()
        expect(self.form_container.locator("#classical")).to_be_visible()
        expect(self.form_container.locator("#bdd")).to_be_visible()
        expect(self.form_container.locator("#project_title")).to_be_visible()
        expect(self.form_container.locator("#demo-btn")).to_be_visible()
        expect(self.form_container.locator("#project-create-btn")).to_be_visible()
        expect(self.page.get_by_text("How to start?")).to_be_visible()

    def fill_project_title(self, target_project_name):
        self.form_container.locator("#project_title").fill(target_project_name)

    def click_create(self):
        self.form_container.get_by_role("button", name="Create").click()


