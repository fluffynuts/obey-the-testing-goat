import django
from django.test import TestCase
from django.conf import settings as django_settings
from superlists import settings as app_settings


class DjangoTest(TestCase):
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
                ALLOWED_HOSTS=["testserver"],
                SITE_ID=1
            )
            django.setup()
        except:
            pass
