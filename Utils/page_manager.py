from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.menu_items import MenuItems
from Pages.my_cart_page import MyCartPage
from Pages.start_page import StartPage


class PageManager:

    def __init__(self):
        self.main_page = MainPage()
        self.start_page = StartPage()
        self.my_cart_page = MyCartPage()
        self.menu_items = MenuItems()
        self.login_page = LoginPage()
