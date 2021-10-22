import django
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django.conf import settings as django_settings
from lists.views import home_page
from superlists import settings as app_settings


class SmokeTests(TestCase):
    # noinspection PyBroadException
    def __init__(self, method_name="runTest"):
        super().__init__(method_name)
        try:
            # FIXME: this is probably only required for pycharm tests
            # and has to be silently ignored when running from the cli
            django_settings.configure(
                DEBUG=True,
                DATABASES=app_settings.DATABASES,
                INSTALLED_APPS=app_settings.INSTALLED_APPS,
                MIDDLEWARE=app_settings.MIDDLEWARE,
                ROOT_URLCONF=app_settings.ROOT_URLCONF,
                STATIC_URL=app_settings.STATIC_URL,
                TEMPLATES=app_settings.TEMPLATES,
                SITE_ID=1
            )
            django.setup()
        except:
            pass

    def test_root_url_resolves_to_home_page(self):
        # arrange
        found = resolve("/")
        # act
        # assert
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_expected_html(self):
        # arrange
        request = HttpRequest()
        # act
        response = home_page(request)
        html: str = response.content.decode("utf8")
        # assert
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))
