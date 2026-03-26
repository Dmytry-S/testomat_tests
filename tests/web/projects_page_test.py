import os

from playwright.sync_api import Page

from src.web.pages.LoginPage import LoginPage
from src.web.pages.ProjectsPage import ProjectsPage
from tests.conftest import Config


def test_search_elements_on_projects_page(page: Page, configs: Config, login):
    # login_page = LoginPage(page)
    # login_page.open()
    # login_page.is_loaded()
    # login_page.login(configs.email, configs.password)

    projects_page = ProjectsPage(page)
    projects_page.is_loaded()
    projects_page.search_project_in_company(os.getenv('TARGET_PROJECT'))
    projects_page.should_be_possible_to_open_free_project()
    projects_page.button_free_plan_should_be_visible()
    projects_page.link_read_docs_is_enabled()
