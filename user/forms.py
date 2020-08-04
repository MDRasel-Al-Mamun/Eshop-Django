from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput, EmailInput, FileInput
from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='User Name: ')
    email = forms.EmailField(max_length=200, label='Email: ')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name: ')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name: ')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'email': EmailInput(attrs={'placeholder': 'email'}),
            'first_name': TextInput(attrs={'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'placeholder': 'phone'}),
            'address': TextInput(attrs={'placeholder': 'address'}),
            'city': TextInput(attrs={'placeholder': 'city'}),
            'country': TextInput(attrs={'placeholder': 'country'}),
            'image': FileInput(attrs={'placeholder': 'image', }),
        }
