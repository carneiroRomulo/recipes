from django.urls import resolve, reverse
from recipes import views

from ..test_recipe_base import RecipeTestBase


class RecipeViewCategoryTest(RecipeTestBase):
    def test_recipe_view_category_function(self):
        view = resolve(reverse('recipes:category', kwargs={'id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_view_category_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'Loads every recipe related to the selected category'
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse('recipes:category', kwargs={'id': 1}))
        context = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
        self.assertEqual(len(context), 1)

    def test_recipe_category_template_dont_load_non_published_recipes(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:category', kwargs={'id': recipe.id}))
        self.assertEqual(response.status_code, 404)

    # def test_recipe_view_category_loads_correct_template(self):
    #     response = self.client.get(
    #         reverse('recipes:category', kwargs={'id': 10000}))
    #     self.assertTemplateUsed(response, 'pages/category.html')
