from django.contrib.auth.models import User
from django import forms


class UserRegisterForms(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
