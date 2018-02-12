from django.shortcuts import render, redirect
'''from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import Http404'''
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Profile
from .forms import UserForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction

def index(request): # Landing page
    context = {}
    return render(request, 'crud/index.html', context)

@login_required
@transaction.atomic
def update_profile(request): # Shows User and Profile form
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('crud:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'crud/registration_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

'''class ProfileView(generic.DetailView): # Shows profile
    model = User
    template_name = 'crud/user_profile.html'
'''
class ProfileCreate(CreateView): # Adds profile
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']
'''
class ProfileUpdate(UpdateView): # Updates profile
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileDelete(DeleteView): # Deletes profile
    model = User
    success_url = reverse_lazy('crud:index')
'''
class LoginForm():
    model = User
    fields = ['email', 'password']

def logout_view(request): # Logs out user
    logout(request)
    return redirect('crud:index')
