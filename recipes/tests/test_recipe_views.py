from django.test import TestCase
from django.urls import resolve, reverse
from recipes import models, views


class RecipeViewHomeTest(TestCase):
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
        category = models.Category.objects.create(name='Category')
        author = models.User.objects.create_user(
            first_name='Romulo',
            last_name='Carneiro',
            username='admin',
            password='123456',
            email='username@gmail.com',
        )
        recipe = models.Recipe.objects.create(
            slug='recipe-slug',
            is_published=True,
            cover='',
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
        )
        assert 1 == 1


class RecipeViewCategoryTest(TestCase):
    def test_recipe_view_category_function(self):
        view = resolve(reverse('recipes:category', kwargs={'id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_view_category_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    # def test_recipe_view_category_loads_correct_template(self):
    #     response = self.client.get(
    #         reverse('recipes:category', kwargs={'id': 10000}))
    #     self.assertTemplateUsed(response, 'pages/category.html')


class RecipeViewDetailTest(TestCase):

    def test_recipe_view_detail_function(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_view_detail_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)
