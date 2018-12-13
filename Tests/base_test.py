import pytest

from Utils.application import Application
from Utils.page_manager import PageManager


class BaseTest:

    @pytest.fixture(scope='function')
    def app(self, request):
        app = Application()

        def fin():
            app.complete()

        request.addfinalizer(fin)

        return app

    @pytest.yield_fixture()
    def pm(self):
        pm = PageManager()
        yield pm
