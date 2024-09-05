import pytest
from playwright.sync_api import expect
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.sanity
def test_validate_login(set_up_admin_page) -> None:
    credentials = {'username': 'admin', 'password': 'password'}
    page = set_up_admin_page
    login_page = AdminLoginPage(page)
    home_page = login_page.submit_login(credentials)
    expect(home_page.rooms_container).to_be_visible()


def test_validate_login_with_invalid_user(set_up_admin_page) -> None:
    credentials = {'username': 'invalidUsername', 'password': 'password'}
    page = set_up_admin_page
    login_page = AdminLoginPage(page)
    home_page = login_page.submit_login(credentials)
    expect(login_page.invalid_username_field).to_be_visible()
    expect(home_page.rooms_container).not_to_be_visible()


def test_validate_login_with_invalid_password(set_up_admin_page) -> None:
    credentials = {'username': 'admin', 'password': 'invalidPassword'}
    page = set_up_admin_page
    login_page = AdminLoginPage(page)
    home_page = login_page.submit_login(credentials)
    expect(login_page.invalid_password_field).to_be_visible()
    expect(home_page.rooms_container).not_to_be_visible()
