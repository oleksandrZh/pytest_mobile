from Helpers.user import User
from Tests.base_test import BaseTest


class TestLoginEdited(BaseTest):
    """User is able to"""

    # run test in command line pytest Tests/login_test_edited.py -v

    def test_login_as_valid_user(self, app):
        """login to application"""
        user = User().set_valid_user()
        app.base_helper.skip_main_page()
        app.login_helper.login_to_app(user)


