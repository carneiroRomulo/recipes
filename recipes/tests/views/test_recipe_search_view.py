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

    def test_recipe_view_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = self.make_recipe(
            slug='one', title=title1, author={'username': 'one'})
        recipe2 = self.make_recipe(
            slug='two', title=title2, author={'username': 'two'})

        search_url = reverse('recipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
