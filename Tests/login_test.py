from Tests.base_test import BaseTest


class TestLogin(BaseTest):
    """WTF?????"""

    # run test in command line pytest Tests/login_test.py -v

    def test_login_as_valid_user(self, app, pm):
        """"""
        app.browser.tap_button(pm.start_page.get_skip_button())
        app.browser.tap_button(pm.main_page.get_menu_button())
        user_name = app.browser.get_text(pm.menu_items.get_profile_name())
        assert user_name == 'Login & Register'

