from Pages.menu_items import MenuItems


class MyCartPage(MenuItems):
    _cart_empty_text = "//*[@resource-id = 'com.ownmettro.androidecommerce:id/empty_cart']"

    def get_cart_empty_cart(self):
        return self._cart_empty_text
