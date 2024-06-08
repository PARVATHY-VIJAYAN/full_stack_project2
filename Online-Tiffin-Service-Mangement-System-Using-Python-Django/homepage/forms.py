from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class UserCreateForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        help_texts = {
                'username': None,
                'email': None,
                'password1':None,
                'password2': None,
            }