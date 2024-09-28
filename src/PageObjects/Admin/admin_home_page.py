# from src.PageObjects.Admin.admin_login_page import AdminLoginPage
# from src.PageObjects.Admin.admin_messages_page import AdminMessagesPage


class AdminHomePage:
    """
    Should only be referencing the Admin Home page
    https://automationintesting.online/#/admin/
    """
    def __init__(self, page):
        self.page = page
        self._create_rooms_btn = page.locator("//*[@id='createRoom']")
        self._inbox_link = page.locator("//*[@href='#/admin/messages']")
        self._logout_btn = page.locator("//*[text()='Logout']")

    @property
    def rooms_container(self):
        return self._create_rooms_btn

    def click_logout_btn(self):
        """Clicks on the Logout button in the Nav Menu"""
        self._logout_btn.click()
        from src.PageObjects.Admin.admin_login_page import AdminLoginPage  # Local import to avoid circular import
        return AdminLoginPage(self.page)

    def click_inbox_link(self):
        """Clicks on the Inbox icon in the Nav Menu"""
        self._inbox_link.click()
        from src.PageObjects.Admin.admin_messages_page import AdminMessagesPage
        return AdminMessagesPage(self.page)
