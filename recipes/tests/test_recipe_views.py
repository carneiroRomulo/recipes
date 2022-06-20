from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


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
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_recipe_view_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        context = response.context['recipes']

        self.assertEqual(len(context), 1)
        self.assertEqual(context.first().title, 'Recipe Title')

    def test_recipe_home_template_dont_load_non_published_recipes(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )


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


class RecipeViewDetailTest(RecipeTestBase):

    def test_recipe_view_detail_function(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_view_detail_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_non_published_recipe(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)


class RecipeViewSearchTest(RecipeTestBase):

    def test_recipe_view_search_function(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_view_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'pages/search.html')
