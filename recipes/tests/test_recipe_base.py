from django.test import TestCase
from recipes import models


class RecipeTestBase(TestCase):
    # Executed before any test
    # def setUp(self) -> None:
    #     return super().setUp()

    # # Executed after any test
    # def tearDown(self) -> None:
    #     return super().tearDown()

    def make_category(self, name='Category'):
        return models.Category.objects.create(name=name)

    def make_author(
        self,
        first_name='Romulo',
        last_name='Carneiro',
        username='admin',
        password='123456',
        email='username@gmail.com',
    ): return models.User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        email=email,
    )

    def make_recipe(
        self,
        slug='recipe-slug',
        is_published=True,
        cover='cover.png',
        category={},
        author={},
        title='Recipe Title',
        description='Recipe Description',
        preparation_time=10,
        preparation_time_unit='Minutos',
        servings=5,
        servings_unit='Porções',
        preparation_steps='Recipe Preparation Steps',
        preparation_steps_is_html=False,
    ):
        return models.Recipe.objects.create(
            slug=slug,
            is_published=is_published,
            cover=cover,
            category=self.make_category(**category),
            author=self.make_author(**author),
            title=title,
            description=description,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
        )
