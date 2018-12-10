from Helpers.appdriver import get_appdriver
from Pages.main_page import MainPage
from Utils.browser import Browser


class Application:

    def __init__(self):
        self.driver = get_appdriver()
        self.main_page = MainPage()
        self.browser = Browser(self.driver)

    def complete(self):
        self.driver.quit()
