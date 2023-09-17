from src.PageObjects.Admin.admin_home_page import AdminHomePage


class AdminLoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_test_id("username")
        self._password = page.get_by_test_id("password")
        self._submit_btn = page.get_by_test_id("submit")
        self._invalid_username = page.locator("//*[@id='username' and contains(@style, 'red')]")
        self._invalid_password = page.locator("//*[@id='password' and contains(@style, 'red')]")

    def input_username(self, username):
        self._username.clear()
        self._username.fill(username)

    def input_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_submit(self):
        self._submit_btn.click()

    def submit_login(self, credentials):
        self.input_username(credentials['username'])
        self.input_password(credentials['password'])
        self.click_submit()
        return AdminHomePage(self.page)

    @property
    def invalid_username_field(self):
        return self._invalid_username

    @property
    def invalid_password_field(self):
        return self._invalid_password
