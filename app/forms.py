from django import forms
# from .models import User

class UserForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)