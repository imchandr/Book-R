

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm


class RegistrationForm(forms.ModelForm):

    first_name = forms.CharField(
        min_length=4, max_length=25, help_text='Required', label='First-Name')
    last_name = forms.CharField(
        min_length=4, max_length=25, help_text='Required', label='Last-Name')
    username = forms.CharField(
        min_length=4, max_length=25, help_text='Required', label='User-Name')
    email = forms.EmailField(
        max_length=50, label='Email', help_text='Required')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirm-Password')

    def __init__(self, *args, **kwargs):
        '''another way to style form elements'''

        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeHolder': 'First name',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeHolder': 'Last name',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['username'].widget.attrs.update({
            'placeHolder': 'User name',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['email'].widget.attrs.update({
            'placeHolder': 'Email',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['password'].widget.attrs.update({
            'placeHolder': 'Password',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['confirm_password'].widget.attrs.update({
            'placeHolder': 'Confirm-Password',
            'class': 'block w-3/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # check if username exist
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError(
                "That username is already taken , please select another ")
        # check if email exist
        email = User.objects.filter(email=email)
        if email:
            raise forms.ValidationError(
                "That email is already taken , please select another ")
        # check password
        if password != confirm_password:
            raise forms.ValidationError(
                "Your password and confirm password do not match!")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-yellow-500 focus:ring-1 focus:ring-yellow-600 focus:ring-opacity-50 rounded-md'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-yellow-500 focus:ring-1 focus:ring-yellow-600 focus:ring-opacity-50 rounded-md'
    }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Registered email-id',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-red-500 focus:ring-1 focus:ring-red-600 focus:ring-opacity-50 rounded-md'
    }))


class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'placeholder': 'New Password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-green-500 focus:ring-1 focus:ring-green-600 focus:ring-opacity-50 rounded-md'
    }))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm New password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-green-500 focus:ring-1 focus:ring-green-600 focus:ring-opacity-50 rounded-md'
    }))

    # def clean_password(self):
    #     cd = self.cleaned_data
    #     if cd['new_password'] != cd['confirm_new_password']:
    #         raise forms.ValidationError('Password Did not match')
    #     return cd['confirm_new_password']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Old Password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-yellow-500 focus:ring-1 focus:ring-yellow-600 focus:ring-opacity-50 rounded-md'
    }))

    new_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'New Password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-yellow-500 focus:ring-1 focus:ring-yellow-600 focus:ring-opacity-50 rounded-md'
    }))
    confirm_password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'block w-4/5 px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-yellow-500 focus:ring-1 focus:ring-yellow-600 focus:ring-opacity-50 rounded-md'
    }))
