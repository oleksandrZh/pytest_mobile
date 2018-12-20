"""Login page"""


class LoginPage:
    #
    _user_ccode = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/user_ccode']"
    #
    _user_email = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/user_email']"
    #
    _user_password = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/user_password']"
    #
    _login_btn = ".//*[@resource-id = 'com.ownmettro.androidecommerce:id/loginBtn']"

    def get_user_ccode(self):
        return self._user_ccode

    def get_user_number(self):
        return self._user_email

    def get_user_password(self):
        return self._user_password

    def get_login_btn(self):
        return self._login_btn
