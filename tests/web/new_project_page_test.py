from faker import Faker
from playwright.sync_api import Page

from src.web.pages.CreatedProjectPage import CreatedProjectPage
from src.web.pages.NewProjectsPage import NewProjectsPage


def test_new_project_page_elements(page: Page, login):
    new_projects = NewProjectsPage(page)
    new_projects.open()
    new_projects.is_loaded()

def test_new_project_creation(page: Page, login):
    new_projects = NewProjectsPage(page)
    new_projects.open()
    new_projects.is_loaded()
    new_projects.fill_project_title(Faker().company())
    new_projects.click_create()

    CreatedProjectPage(page).is_loaded()
