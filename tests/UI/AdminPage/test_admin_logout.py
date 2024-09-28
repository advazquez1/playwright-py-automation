import pytest
from playwright.sync_api import expect
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.regression
class TestAdminLogout:
    @pytest.mark.sanity
    @pytest.mark.parametrize('credentials', [('admin', 'password')])
    def test_validate_logout(self, credentials, set_up_admin_page) -> None:
        page = set_up_admin_page
        login_page = AdminLoginPage(page)
        home_page = login_page.submit_login(credentials)
        expect(home_page.rooms_container).to_be_visible()
        login_page = home_page.click_logout_btn()
        expect(login_page.login_container).to_be_visible()
