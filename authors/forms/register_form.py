from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):
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

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid')
        return email

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
