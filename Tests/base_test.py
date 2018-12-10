import pytest

from Utils.application import Application


class BaseTest():
    @pytest.fixture(scope='function')
    def app(self, request):
        app = Application()

        def fin():
            app.complete()

        request.addfinalizer(fin)

        return app
