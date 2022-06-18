from django import forms
from captcha.fields import CaptchaField

class RegisterUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    captcha = CaptchaField()
