class AdminHomePage:
    def __init__(self, page):
        self.page = page
        self._rooms_container = page.locator("(//*[@class='container'])[1]")

    @property
    def rooms_container(self):
        return self._rooms_container
