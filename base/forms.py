from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class RegisterUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    captcha = CaptchaField()
