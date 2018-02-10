from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio', 'gender')
