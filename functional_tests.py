import subprocess
import time
from urllib.error import URLError

from selenium import webdriver
from unittest import TestCase, main as test_main
from urllib.request import urlopen

from selenium.webdriver.common.keys import Keys

server_url = "http://localhost:8000"


class TestFunctional(TestCase):
    def setUp(self):
        self.cmd = None
        if self.server_is_not_running():
            self.cmd = subprocess.Popen("virtualenv/scripts/python manage.py runserver")
        self.browser = webdriver.Firefox()

    # noinspection PyBroadException
    def tearDown(self):
        try:
            self.browser.quit()
        except:
            pass
        if self.cmd is not None:
            self.cmd.kill()

    def server_is_not_running(self):
        try:
            urlopen(server_url)
            return False
        except URLError:
            return True

    def test_should_be_able_to_start_a_list_and_retrieve_it_later(self):
        # arrange
        browser = self.browser
        # act
        # user visits the site's home page
        browser.get(server_url)
        # assert

        # she should see the page title
        self.assertIn("To-Do", browser.title)
        header = browser.find_element_by_tag_name("h1")
        self.assertIn("To-Do", header.text)

        # she should be asked to enter a to-do item immediately
        input_box = browser.find_element_by_id("new_item")
        self.assertEqual(
            input_box.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # she types "Buy peacock feathers" into a text box (she makes fishing lures)
        input_box.send_keys("Buy peacock feathers")

        # she hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        # FIXME: this will cause flaky tests, but we have to wait for the
        # page to reload
        time.sleep(1)

        table = browser.find_element_by_id("list_table")
        self.assertIsNotNone(table)
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            "new to-do item did not appear in the rows"
        )

        # there is still a text box to add another item
        # she adds "Use peacock feathers to make a fly"

        # the page updates again and now both items are in the list

        # the site "remembers the list" via url parameters
        # there should be some text explaining this
        # - she visits that url - her to-do list is still there

        # she quits
        # technically, we could leave this out as the fixture cleans up, but it's part of the story (:
        browser.quit()
        self.fail("finish the test!")


if __name__ == "__main__":
    test_main()
