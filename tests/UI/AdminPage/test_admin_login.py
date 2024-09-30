import pytest
from playwright.sync_api import expect, Page
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.sanity
class TestAdminLogin:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page, set_up_admin_page):
        self.login_page = AdminLoginPage(page)

    @pytest.mark.parametrize('credentials', [('admin', 'password')])
    def test_validate_login(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(home_page.rooms_container).to_be_visible()

    @pytest.mark.parametrize('credentials', [('invalidUsername', 'password')])
    def test_validate_login_with_invalid_user(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(self.login_page.invalid_username_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('admin', 'invalidPassword')])
    def test_validate_login_with_invalid_password(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(self.login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('', '')])
    def test_validate_login_with_empty_credentials(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(self.login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()

    @pytest.mark.parametrize('credentials', [('\' OR \'1\'=\'1\'', 'password')])
    def test_validate_login_with_sql_injection(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(self.login_page.invalid_password_field).to_be_visible()
        expect(home_page.rooms_container).not_to_be_visible()
