from unittest import TestCase

from authors.forms import RegisterForm
from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('first_name',          'Ex.: Romulo'),
        ('last_name',           'Ex.: Carneiro'),
        ('username',            'Your username'),
        ('email',               'Your e-mail'),
        ('password',            'Your password'),
        ('confirm_password',    'Confirm password'),
    ])
    def test_fields_placeholder_is_correct(self, field, needed_field):
        form = RegisterForm()
        current_field = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_field, needed_field)

    @parameterized.expand([
        ('first_name', 'Type only letters'),
        ('last_name',  'Type only letters'),
    ])
    def test_fields_help_text_is_correct(self, field, needed_field):
        form = RegisterForm()
        current_field = form[field].field.help_text
        self.assertEqual(current_field, needed_field)

    @parameterized.expand([
        ('first_name',          'First Name'),
        ('last_name',           'Last Name'),
        ('username',            'Username'),
        ('email',               'E-mail'),
        ('password',            'Password'),
        ('confirm_password',    'Confirm Password'),
    ])
    def test_fields_label_is_correct(self, field, needed_field):
        form = RegisterForm()
        current_field = form[field].field.label
        self.assertEqual(current_field, needed_field)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            'first_name': 'Paulo',
            'last_name': 'Brandão',
            'username': 'pauloCarneiro',
            'email': 'paulo@paulo.com',
            'password': 'Paulo123',
            'confirm_password': 'Paulo123',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('first_name', 'This field is required.'),
        ('last_name', 'This field is required.'),
        ('username', 'This field is required.'),
        ('email', 'This field is required.'),
        ('password', 'This field is required.'),
        ('confirm_password', 'This field is required.'),
    ])
    def test_fields_cannot_be_empty(self, field, message):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(message, response.context['form'].errors.get(field))
        # self.assertIn(message, response.content.decode('utf-8'))

    def test_username_field_min_length_shold_be_6(self):
        self.form_data['username'] = 'joa'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Ensure this value has at least 6 characters (it has 3).'
        self.assertIn(msg, response.context['form'].errors.get('username'))
        # self.assertIn(msg, response.content.decode('utf-8'))

    def test_username_field_max_length_should_be_40(self):
        self.form_data['username'] = 'A' * 41
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Ensure this value has at most 40 characters (it has 41).'

        self.assertIn(msg, response.context['form'].errors.get('username'))
        # self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        msg = (
            ('Password must have at least 8 characters long, '
             'allowed are [a-z][A-Z][0-9]')
        )
        url = reverse('authors:create')

        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertNotIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = "Abc12"
        self.form_data['confirm_password'] = "Abc12"
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        # Check if password is valid
        url = reverse('authors:create')
        msg = 'Passwords do not match'

        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertNotIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        self.form_data['confirm_password'] = '@A123abc1235'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.context['form'].errors.get('password'))
        # self.assertIn(msg, response.content.decode('utf-8'))

    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('authors:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
