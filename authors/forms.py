import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# def add_attr(field, attr_name, attr_new_value):
#   existing_attr = field.widget.attrs.get(attr_name, '')
#   field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            ('Password must have at least 8 characters long, '
             'allowed are [a-z][A-Z][0-9]'),
            code='invalid',
        )


class RegisterForm(forms.ModelForm):
    # First way to modify forms. Can be used to add widgets in existing fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add_attr(self.fields['username'], 'placeholder', 'Your username')

    # Second way to modify forms. Can also create new fields.
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Romulo'}),
        label='First Name',
        help_text='Type only letters',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Carneiro'}),
        label='Last Name',
        help_text='Type only letters',
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username'}),
        label='Username',
        min_length=6,
        max_length=40,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your e-mail'}),
        label='E-mail',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
        label='Password',
        validators=[strong_password],
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        label='Confirm Password',
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            password_confirmation_error = ValidationError(
                'Passwords do not match',
                code='invalid',
            )
            # Errors can be chained in a list, like in "confirm_password"
            raise ValidationError({
                'password': password_confirmation_error,
                'confirm_password': [password_confirmation_error],
            })

        return cleaned_data
