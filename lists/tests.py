from django.urls import resolve

from lists.django_tests import DjangoTest
from lists.models import Item
from lists.views import home_page


class SmokeTests(DjangoTest):
    # noinspection PyBroadException
    def test_root_url_resolves_to_home_page(self):
        # arrange
        found = resolve("/")
        # act
        # assert
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_expected_html(self):
        # arrange
        # act
        response = self.client.get("/")
        # assert
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        # arrange
        # act
        response = self.client.post("/", data={"item_text": "A new list item"})
        # assert
        self.assertIn("A new list item", response.content.decode())
        self.assertTemplateUsed(response, "home.html")


class ItemModelTest(DjangoTest):
    # TODO: pick up from here
    def test_saving_and_retrieving_items(self):
        # arrange
        first_item = Item()
        first_item.text = "The first item"
        first_item.save()

        second_item = Item()
        second_item.text = "The second item"
        second_item.save()

        # act
        saved_items = Item.objects.all()
        # assert
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].text, "The first item")
        self.assertEqual(saved_items[1].text, "The second item")
