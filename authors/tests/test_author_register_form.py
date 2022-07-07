from unittest import TestCase

from authors.forms import RegisterForm
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
