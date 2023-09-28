import pytest
from playwright.sync_api import expect
from src.PageObjects.Admin.admin_login_page import AdminLoginPage


@pytest.mark.sanity
def test_validate_message_received(set_up_admin_page, submit_message_api) -> None:
    credentials = {'username': 'admin', 'password': 'password'}
    page = set_up_admin_page
    response = submit_message_api
    login_page = AdminLoginPage(page)
    admin_home_page = login_page.submit_login(credentials)
    expect(admin_home_page.rooms_container).to_be_visible()
    admin_messages_page = admin_home_page.click_inbox_link()
    expect(admin_messages_page.messages_container).to_be_visible()
    admin_messages_page.click_message_by_subject(response['subject'])
    expect(admin_messages_page.messages_modal).to_be_visible()
