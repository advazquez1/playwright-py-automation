import pytest
from playwright.sync_api import expect, Page
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.sanity
class TestAdminMessages:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page, set_up_admin_page):
        self.login_page = AdminLoginPage(page)

    @pytest.mark.parametrize('credentials', [('admin', 'password')])
    def test_validate_message_received(self, credentials, submit_message_api) -> None:
        response = submit_message_api
        admin_home_page = self.login_page.submit_login(credentials)
        expect(admin_home_page.rooms_container).to_be_visible()
        admin_messages_page = admin_home_page.click_inbox_link()
        expect(admin_messages_page.messages_container).to_be_visible()
        admin_messages_page.click_message_by_subject(response['subject'])
        expect(admin_messages_page.messages_modal).to_be_visible()
