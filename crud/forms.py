from django import forms
from django.contrib.auth.models import User

from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="first_name", max_length=30)
    last_name = forms.CharField(label="last_name", max_length=30)
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    email = forms.EmailField(label="email", max_length=254)
    image = forms.ImageField(label="image", max_length=100)
    bio = forms.CharField(label="bio", widget=forms.Textarea)
    gender = forms.CharField(label="gender", max_length=20)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
