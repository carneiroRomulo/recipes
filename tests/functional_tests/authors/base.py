from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser


class AuthorsBaseTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser("--headless", "--no-sandbox")
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
