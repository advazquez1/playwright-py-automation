
class AdminMessagesPage:
    """
        Should only be referencing the Admin Messages page
        https://automationintesting.online/#/admin/messages
    """
    def __init__(self, page):
        self.page = page
        self._messages_container = page.locator("//*[@class='messages']")
        self._messages_modal = page.locator("//*[@data-testid='message']")

    @property
    def messages_container(self):
        return self._messages_container

    @property
    def messages_modal(self):
        return self._messages_modal

    def click_message_by_subject(self, subject: str, index: int = 1):
        """
        Clicks the message by subject.
        :param subject: The subject title to use reference on which message to select
        :param index: Index position if there are multiple messages with same subject title. Defaults to first one
        :return:
        """
        message_locator = \
            (self.page.locator(f"(//*[contains(@data-testid, 'messageDescription')]/p[text()='{subject}'])[{index}]"))
        message_locator.click()
