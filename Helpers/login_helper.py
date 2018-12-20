from Helpers.base_helper import BaseHelper


class LoginHelper(BaseHelper):
    def __init__(self, driver):
        super().__init__(driver)

    def login_to_app(self, user):
        self.browser.tap_button(self.pm.main_page.get_menu_button())
        self.browser.tap_button(self.pm.menu_items.get_profile_image())
        self.browser.clear_field(self.pm.login_page.get_user_ccode())
        self.browser.enter_value_to_field(self.pm.login_page.get_user_ccode(), user.get_ccode())
        self.browser.enter_value_to_field(self.pm.login_page.get_user_number(), user.get_user_phone_number())
        self.browser.enter_value_to_field(self.pm.login_page.get_user_password(), user.get_user_password())
        self.browser.tap_back_button()
        self.browser.tap_button(self.pm.login_page.get_login_btn())
