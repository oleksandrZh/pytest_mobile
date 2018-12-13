from Helpers.appdriver import get_appdriver
from Utils.browser import Browser


class Application:

    def __init__(self):
        self.driver = get_appdriver()
        self.browser = Browser(self.driver)

    def complete(self):
        self.driver.quit()
