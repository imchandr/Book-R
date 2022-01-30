
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'User-Name',
        "class":"w-full rounded px-3 border border-gray-500 pt-5 pb-2 focus:outline-none input active:outline-none"}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        "class":"w-full rounded px-3 border border-gray-500 pt-5 pb-2 focus:outline-none input active:outline-none"}))
    
    