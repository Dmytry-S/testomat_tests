from playwright.sync_api import Page, expect


class CreatedProjectPage:
    def __init__(self, page:Page):
        self.page = page

    def is_loaded(self):
        expect(self.page.locator(".sticky-header")).to_be_visible()
        expect(self.page.locator("#item-title")).to_be_visible()
