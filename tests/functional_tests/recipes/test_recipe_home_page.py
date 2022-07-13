from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from recipes.tests.test_recipe_base import RecipeMixin

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest, RecipeMixin):
    def test_recipe_home_page_without_recipes(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here', body.text)

    @patch('recipes.views.RECIPES_PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipe(self):
        recipes = self.make_recipe_batch(20)

        title_needed = 'This is what I needed'
        recipes[0].title = title_needed
        recipes[0].save()

        # User open webpage
        self.browser.get(self.live_server_url)

        # See search field with the text "Search for a recipe..."
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe..."]'
        )

        # Click on field and type "Recipe title 1" to find the
        # recipe with this title
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # The user see what he was looking for
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text
        )
