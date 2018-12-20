class User:
    """Yeap it is f***ing hardcode"""

    _user_name = ''
    _user_phone_number = ''
    _user_ccode = ''
    _user_password = ''
    _user_email = ''

    def get_ccode(self):
        return self._user_ccode

    def get_user_phone_number(self):
        return self._user_phone_number

    def get_user_password(self):
        return self._user_password

    def set_valid_user(self):
        self._user_email = 'alex.workqa@gmail.com'
        self._user_name = 'alex'
        self._user_ccode = '+38'
        self._user_phone_number = '0669059301'
        self._user_password = 'qwerty123'
        return self
