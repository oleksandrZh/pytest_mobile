from Utils.browser import Browser
from Utils.page_manager import PageManager


class BaseHelper(object):

    def __init__(self, driver):
        self.browser = Browser(driver)
        self.pm = PageManager()

    def skip_main_page(self):
        self.browser.tap_button(self.pm.start_page.get_skip_button())
