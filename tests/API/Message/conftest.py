import pytest
from src.utils.REST.rest_automation_online import RestAutomationOnline


@pytest.fixture()
def submit_message_api() -> dict:
    request = RestAutomationOnline()
    response = request.rest_submit_message()
    return response


@pytest.fixture()
def get_message_api() -> dict:
    request = RestAutomationOnline()
    response = request.rest_get_message()
    return response


@pytest.fixture()
def get_message_count_api() -> dict:
    request = RestAutomationOnline()
    response = request.rest_get_message_count()
    return response
