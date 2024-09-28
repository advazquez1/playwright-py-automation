# from src.PageObjects.Admin.admin_home_page import AdminHomePage


class AdminLoginPage:
    """
        Should only be referencing the Admin Login page
        https://automationintesting.online/#/admin
    """
    def __init__(self, page):
        self.page = page
        self._login_header = page.locator("//*[@data-testid='login-header']")
        self._username = page.get_by_test_id("username")
        self._password = page.get_by_test_id("password")
        self._submit_btn = page.get_by_test_id("submit")
        self._invalid_username = page.locator("//*[@id='username' and contains(@style, 'red')]")
        self._invalid_password = page.locator("//*[@id='password' and contains(@style, 'red')]")

    @property
    def login_container(self):
        return self._login_header

    def input_username(self, username: str):
        self._username.clear()
        self._username.fill(username)

    def input_password(self, password: str):
        self._password.clear()
        self._password.fill(password)

    def click_submit(self):
        self._submit_btn.click()

    def submit_login(self, credentials: tuple):
        """
        Takes the given username and password credentials and clicks submit
        :param credentials: key value tuple pair containing a username and password
        :return:
        """
        self.input_username(credentials[0])
        self.input_password(credentials[1])
        self.click_submit()
        from src.PageObjects.Admin.admin_home_page import AdminHomePage  # Local import
        return AdminHomePage(self.page)

    @property
    def invalid_username_field(self):
        return self._invalid_username

    @property
    def invalid_password_field(self):
        return self._invalid_password
