from django.urls import resolve, reverse
from recipes import views

from ..test_recipe_base import RecipeTestBase


class RecipeViewSearchTest(RecipeTestBase):
    def test_recipe_view_search_function(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_view_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'pages/search.html')

    def test_recipe_view_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_view_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=Test'
        response = self.client.get(url)
        self.assertIn('Search for &quot;Test&quot;',
                      response.content.decode('utf-8'))
