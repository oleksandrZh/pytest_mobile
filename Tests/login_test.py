from Tests.base_test import BaseTest


class TestLogin(BaseTest):
    """User is able to"""

    # run test in command line pytest Tests/login_test.py -v

    def test_login_as_valid_user(self, app, pm):
        """login to app with valid user creds"""
        app.browser.tap_button(pm.start_page.get_skip_button())
        app.browser.tap_button(pm.main_page.get_menu_button())
        user_name = app.browser.get_text(pm.menu_items.get_profile_name())
        assert user_name == 'Login & Register'
        app.browser.tap_button(pm.menu_items.get_profile_image())
        app.browser.clear_field(pm.login_page.get_user_ccode())
        app.browser.enter_value_to_field(pm.login_page.get_user_ccode(), '+38')
        app.browser.enter_value_to_field(pm.login_page.get_user_number(), '0669059301')
        app.browser.enter_value_to_field(pm.login_page.get_user_password(), 'qwerty123')
        app.browser.tap_back_button()
        app.browser.tap_button(pm.login_page.get_login_btn())
        app.browser.tap_button(pm.main_page.get_menu_button())
        user_name = app.browser.get_text(pm.menu_items.get_profile_name())
        user_email = app.browser.get_text(pm.menu_items.get_profile_email())
        assert user_name == 'alex test'
        assert user_email == 'alex.workqa@gmail.com'
