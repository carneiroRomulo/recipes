from unittest.mock import patch

from django.urls import resolve, reverse
from recipes import views

from ..test_recipe_base import RecipeTestBase


# @skip('WIP')
class RecipeViewHomeTest(RecipeTestBase):
    def test_recipe_view_home_function(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_view_home_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_view_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_view_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        context = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(context), 1)

    def test_recipe_home_template_dont_load_non_published_recipes(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_is_paginated(self):
        self.make_recipe_batch(10)

        with patch('recipes.views.RECIPES_PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 4)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 3)
            self.assertEqual(len(paginator.get_page(4)), 1)

    def test_invalid_page_query_uses_page_one(self):
        self.make_recipe_batch(10)

        with patch('recipes.views.RECIPES_PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home') + '?page=1A')
            self.assertEqual(response.context['recipes'].number, 1)

            response = self.client.get(reverse('recipes:home') + '?page=2')
            self.assertEqual(response.context['recipes'].number, 2)
