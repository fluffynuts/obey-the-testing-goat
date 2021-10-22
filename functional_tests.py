import subprocess
from selenium import webdriver
from unittest import TestCase, main as test_main


class TestFunctional(TestCase):
    def setUp(self):
        self.cmd = subprocess.Popen("virtualenv/scripts/python manage.py runserver")
        self.browser = webdriver.Firefox()

    # noinspection PyBroadException
    def tearDown(self):
        try:
            self.browser.quit()
        except:
            pass
        self.cmd.kill()

    def test_should_be_able_to_start_a_list_and_retrieve_it_later(self):
        # arrange
        browser = self.browser
        # act
        # user visits the site's home page
        browser.get("http://localhost:8000")
        # assert

        # she should see the page title
        self.assertIn("To-Do", browser.title)

        # she should be asked to enter a to-do item immediately

        # she types "Buy peacock feathers" into a text box (she makes fishing lures)

        # she hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

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
