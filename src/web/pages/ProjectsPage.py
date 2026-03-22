import os

from playwright.sync_api import Page, expect


class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self):
        expect(self.page.locator(".common-flash-success")).to_have_text("Signed in successfully")

    def search_project(self, target_project: str):
        self.page.locator("#content-desktop #search").fill(target_project)

    def search_project_in_company(self, target_project: str):
        self.search_project(target_project)

        expect(self.page.get_by_role("heading", name=os.getenv('TARGET_PROJECT'))).to_be_visible()

    def select_free_project(self):
        self.page.locator("#company_id").click()
        self.page.locator("#company_id").select_option("Free Projects")

    def should_be_possible_to_open_free_project(self):
        self.select_free_project()
        self.search_project(os.getenv('TARGET_PROJECT'))

        expect(self.page.get_by_role("heading", name=os.getenv('TARGET_PROJECT'))).to_be_hidden()
        expect(self.page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=6000)

    def button_free_plan_should_be_visible(self):
        expect(self.page.locator("#content-desktop .tooltip-project-plan")).to_be_visible()

    def link_read_docs_is_enabled(self):
        self.select_free_project()

        expect(self.page.locator("[href='https://docs.testomat.io'].underline")).to_be_enabled()
