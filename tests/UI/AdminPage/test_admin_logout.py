import pytest
from playwright.sync_api import expect, Page
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.regression
class TestAdminLogout:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page, set_up_admin_page):
        self.login_page = AdminLoginPage(page)

    @pytest.mark.sanity
    @pytest.mark.parametrize('credentials', [('admin', 'password')])
    def test_validate_logout(self, credentials):
        home_page = self.login_page.submit_login(credentials)
        expect(home_page.rooms_container).to_be_visible()
        login_page = home_page.click_logout_btn()
        expect(login_page.login_container).to_be_visible()
