from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
