from Pages.mycart_page import MyCartPage
from Tests.base_test import BaseTest
from Pages.main_page import *
from Pages.start_page import *
import logging


class TestAddToCart(BaseTest):
    """User is able to"""

    # run test in command line pytest Tests/add_item_to_cart.py -v

    def test_add_to_cart_item(self, app):
        """add item to the empty cart"""
        logging.basicConfig(filename='/home/osboxes/pytest_mobile/logs/test.log', level=logging.DEBUG, filemode="w")
        start_page = StartPage()
        main_page = MainPage()
        cart_page = MyCartPage()
        app.browser.tap_button(start_page.get_skip_button())
        app.browser.tap_button(main_page.get_cart_button())
        result = app.browser.get_text(cart_page.get_cart_empty_cart())
        assert result == "Your Cart is Empty"
