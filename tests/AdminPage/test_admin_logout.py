from playwright.sync_api import Page, expect
from src.PageObjects.Admin.admin_login_page import AdminLoginPage
from src.PageObjects.Admin.admin_login_page import AdminHomePage


def test_validate_logout(set_up_admin_page) -> None:
    credentials = {'username': 'admin', 'password': 'password'}
    page = set_up_admin_page
    login_page = AdminLoginPage(page)
    home_page = login_page.submit_login(credentials)
    expect(home_page.rooms_container).to_be_visible()
