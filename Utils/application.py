from Helpers.appdriver import get_appdriver
from Helpers.base_helper import BaseHelper
from Utils.browser import Browser
from Helpers.login_helper import LoginHelper


class Application:

    def __init__(self):
        self.driver = get_appdriver()
        self.browser = Browser(self.driver)
        self.base_helper = BaseHelper(self.driver)
        self.login_helper = LoginHelper(self.driver)

    def complete(self):
        self.driver.quit()
