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
            'username': 'paulo',
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

        # self.assertIn(message, response.content.decode('utf-8'))
        self.assertIn(message, response.context['form'].errors.get(field))
