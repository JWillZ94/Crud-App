from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput, help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio', 'gender')

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
