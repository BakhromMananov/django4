from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    first_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'First Name'}))
    last_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'Last Name'}))
    user_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'Username'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'register-control', 'placeholder': 'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'register-control'}),
            'last_name': forms.TextInput(attrs={'class': 'register-control'}),
            'user_name': forms.TextInput(attrs={'class': 'register-control'}),
            'email': forms.EmailInput(attrs={'class': 'register-control'}), 
            'password1': forms.PasswordInput(attrs={'class': 'register-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'register-control'})
        }



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'login-control', 'placeholder': 'Enter password'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-control', 'placeholder': 'Enter password'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = {
            'first_name',
            'last_name',
            'username',
            'email'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }
