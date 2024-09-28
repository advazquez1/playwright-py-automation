import pytest
from src.utils.REST.rest_automation_online import RestAutomationOnline


@pytest.fixture()
def set_up_admin_page(page) -> None:
    page.goto("https://automationintesting.online/#/admin")
    yield page


@pytest.fixture()
def submit_message_api() -> str:
    request = RestAutomationOnline()
    response = request.rest_submit_message()
    return response
