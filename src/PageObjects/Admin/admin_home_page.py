from src.PageObjects.Admin.admin_messages_page import AdminMessagesPage


class AdminHomePage:
    def __init__(self, page):
        self.page = page
        self._rooms_container = page.locator("(//*[@class='container'])[1]")
        self._inbox_link = page.locator("//*[@href='#/admin/messages']")

    @property
    def rooms_container(self):
        return self._rooms_container

    def click_inbox_link(self):
        """Clicks on the Inbox icon in the Nav Menu"""
        self._inbox_link.click()
        return AdminMessagesPage(self.page)
