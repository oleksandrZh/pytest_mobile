from Tests.base_test import BaseTest


class TestAndroidSimple(BaseTest):
    """Simple launch test"""

    # run test in command line pytest Tests/simple_test.py

    def test_launch_app_test(self, app, pm):
        """should be passed """
        app.browser.tap_button(pm.start_page.get_skip_button())
        app_name = app.browser.get_text(pm.main_page.get_toolbar_text())
        assert app_name == "Ownmetrro"
