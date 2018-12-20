"""Menu items like home, my messages etc."""


class MenuItems(object):
    _home_item = ".//*[contains(text,'Home']"

    _back_button = "//*[@class='android.widget.ImageButton']"

    _profile_name = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/drawer_profile_name']"

    _profile_image = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/drawer_profile_image']"

    _profile_email = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/drawer_profile_email']"

    def get_home_button(self):
        return self._home_item

    def get_back_button(self):
        return self._back_button

    def get_profile_name(self):
        return self._profile_name

    def get_profile_image(self):
        return self._profile_image

    def get_profile_email(self):
        return self._profile_email
