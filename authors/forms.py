from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_value):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()


class RegisterForm(forms.ModelForm):
    # First way to modify forms. Can be used to add widgets in existing fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_attr(self.fields['username'], 'placeholder', 'Your username')
        add_attr(self.fields['email'], 'placeholder', 'Your e-mail')

    # Second way to modify forms. Can also create new fields.
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password',
            'class': 'password-field'
        }),
        error_messages={
            'required': 'Password must not be empty',
        },
        help_text='Password must have at least one uppercase letter, \
                    one lowercase letter and one number. \
                    The length should be at least 8 characters long.',
        label='Password',
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
            'class': 'password-field'
        }),
        error_messages={
            'required': 'Password must not be empty',
        },
        label='Confirm Password',
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

        # Third way to modify forms
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'E-mail',
        }
        help_texts = {
            'first_name': 'Type only letters',
            'last_name': 'Type only letters',
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty'
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex.: Romulo',
                'class': 'input text-input',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ex.: Carneiro',
                'class': 'input text-input',
            }),

        }
