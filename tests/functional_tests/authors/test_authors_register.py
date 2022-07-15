from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorsBaseTest


class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]')

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )
        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('test@test')

        callback(form)
        return form

    def test_empty_first_name_error_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: Romulo')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[1]/ul'
            )
            self.assertEqual('This field is required.', error.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Carneiro')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[2]/ul'
            )
            self.assertEqual('This field is required.', error.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form):
            username_field = self.get_by_placeholder(form, 'Your username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[3]/ul'
            )
            self.assertEqual('This field is required.', error.text)
        self.form_field_test_with_callback(callback)

    def test_empty_password_error_message(self):
        def callback(form):
            password_field = self.get_by_placeholder(form, 'Your password')
            password_field.send_keys(' ')
            password_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[5]/ul'
            )
            self.assertEqual('This field is required.', error.text)
        self.form_field_test_with_callback(callback)

    def test_empty_confirm_password_error_message(self):
        def callback(form):
            confirm_password_field = self.get_by_placeholder(
                form, 'Confirm password')
            confirm_password_field.send_keys(' ')
            confirm_password_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[6]/ul'
            )
            self.assertEqual('This field is required.', error.text)
        self.form_field_test_with_callback(callback)

    def test_empty_email_error_message(self):
        def callback(form):
            email_field = self.get_by_placeholder(form, 'Your e-mail')
            email_field.send_keys(' ')
            email_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[4]/ul'
            )
            self.assertEqual('Enter a valid email address.', error.text)
        self.form_field_test_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            password_field = self.get_by_placeholder(form, 'Your password')
            confirm_password_field = self.get_by_placeholder(
                form, 'Confirm password')

            password_field.send_keys('P@ssw0rd')
            confirm_password_field.send_keys('P@ssw0rd_different')
            confirm_password_field.send_keys(Keys.ENTER)

            # Check if error is showed
            error = self.browser.find_element(
                By.XPATH,
                '/html/body/main/div[2]/form/div[1]/div[6]/ul'
            )
            self.assertEqual('Passwords do not match', error.text)
        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )
        self.get_by_placeholder(form, 'Ex.: Romulo').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Carneiro').send_keys('Last Name')
        self.get_by_placeholder(
            form, 'Your username').send_keys('romuloCarneiro')
        self.get_by_placeholder(
            form, 'Your e-mail').send_keys('email@valid.com')
        self.get_by_placeholder(form, 'Your password').send_keys('P@ssw0rd')
        self.get_by_placeholder(form, 'Confirm password').send_keys('P@ssw0rd')

        form.submit()
        self.assertIn(
            'User created, please log in.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
