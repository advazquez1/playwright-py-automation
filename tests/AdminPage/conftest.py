import pytest


@pytest.fixture()
def set_up_admin_page(page) -> None:
    page.goto("https://automationintesting.online/#/admin")
    yield page
