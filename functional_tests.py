import os
import subprocess

from selenium import webdriver
from pytest import fixture, mark


class TestFunctional:
    @fixture
    def browser(self):
        browser = webdriver.Firefox()
        yield browser
        browser.close()

    @fixture
    def server(self):
        cmd = subprocess.Popen("virtualenv/scripts/python manage.py runserver")
        yield cmd
        cmd.kill()

    def test_should_start_basic_django_site(self, browser, server):
        # arrange
        # act
        browser.get("http://localhost:8000")
        # assert
        assert "Django" in browser.title
