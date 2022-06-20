from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url(self):
        url = reverse('recipes:category', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/category/1/')

    def test_recipe_detail_url(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')

    def test_recipe_search_url(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipe/search/')
