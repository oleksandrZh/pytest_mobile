"""Main page appears if user launch app"""


class MainPage:
    # menu button
    _menu_button = "//*[@class='android.widget.ImageButton']"
    # my cart button
    _cart_button = "//*[@resource-id = 'com.ownmettro.androidecommerce:id/toolbar_ic_cart']"
    #toolbar
    _toolbar_text = "//*[@content-desc = 'DrawerOpen']/following-sibling::*[1]"

    def get_menu_button(self):
        return self._menu_button

    def get_cart_button(self):
        return self._cart_button

    def get_toolbar_text(self):
        return self._toolbar_text


