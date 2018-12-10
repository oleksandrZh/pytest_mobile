from Tests.base_test import BaseTest
from Pages.main_page import *
from Pages.start_page import *


class TestAndroidSimple(BaseTest):
    """Simple launch test"""

    # run test in command line pytest Tests/simple_test.py

    def test_launch_app_test(self, app):
        """should be passed """
        start_page = StartPage()
        main_page = MainPage()
        app.browser.tap_button(start_page.get_skip_button())
        app_name = app.browser.get_text(main_page.get_toolbar_text())
        assert app_name == "Ownmetrro"
