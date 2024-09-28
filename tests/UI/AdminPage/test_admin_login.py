import pytest
from playwright.sync_api import expect
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.sanity
class TestAdminLogin:

    @pytest.mark.parametrize('credentials', [('admin', 'password')])
    def test_validate_login(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(home_page.rooms_container).to_be_visible()

    @pytest.mark.parametrize('credentials', [('invalidUsername', 'password')])
    def test_validate_login_with_invalid_user(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(login_page.invalid_username_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('admin', 'invalidPassword')])
    def test_validate_login_with_invalid_password(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('', '')])
    def test_validate_login_with_empty_credentials(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('\' OR \'1\'=\'1\'', 'password')])
    def test_validate_login_with_sql_injection(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()
