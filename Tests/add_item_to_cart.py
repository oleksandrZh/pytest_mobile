from Tests.base_test import BaseTest
import logging


class TestAddToCart(BaseTest):
    """User is able to"""

    # run test in command line pytest Tests/add_item_to_cart.py -v

    def test_add_to_cart_item(self, app, pm):
        """add item to the empty cart"""
        logging.basicConfig(filename='/home/osboxes/pytest_mobile/logs/test.log', level=logging.DEBUG, filemode="w")
        app.browser.tap_button(pm.start_page.get_skip_button())
        app.browser.tap_button(pm.main_page.get_cart_button())
        result = app.browser.get_text(pm.my_cart_page.get_cart_empty_cart())
        assert result == "Your Cart is Empty"
        app.browser.tap_button(pm.menu_items.get_back_button())
