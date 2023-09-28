
class AdminMessagesPage:

    def __init__(self, page):
        self.page = page
        self._messages_container = page.locator("//*[@class='messages']")
        # self._messages_subject_header = page.locator(f"//*[@data-testid='messageDescription0']/p[text()='{subject}']")
        self._messages_modal = page.locator("//*[@data-testid='message']")

    @property
    def messages_container(self):
        return self._messages_container

    @property
    def messages_modal(self):
        return self._messages_modal

    def click_message_by_subject(self, subject):
        message_locator = self.page.locator(f"//*[contains(@data-testid, 'messageDescription')]/p[text()='{subject}']")
        message_locator.click()
