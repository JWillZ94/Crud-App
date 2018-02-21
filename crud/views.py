from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction

def index(request): # Landing page
    context = {}
    return render(request, 'crud/index.html', context)

@transaction.atomic
def update_profile(request): # Shows User and Profile form
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        username = request.POST.get('username', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        bio = request.POST.get('bio', None)
        image = request.FILES.get('image', None)
        gender = request.POST.get('gender', None)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile) #
        print (user_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
            user.set_password(password)
            user.save()
            profile_form.save()
            profile = Profile.objects.create(user=request.user, bio=bio, image=image, gender=gender)
            messages.success(request, 'Your profile was successfully created!')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('crud:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'crud/registration_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_user(request): # Logs user in page
    if request.method == 'POST':
        login_form = LoginForm(request.POST, instance=request.user)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crud:profile')
        else:
            messages.error(request, 'Username and/or password do not match.')
    else:
        login_form = LoginForm()
    return render(request, 'crud/login_form.html', { 'login_form': login_form })

# @login_required() # redirect_field_name='next', login_url='crud:profile'
def profile(request, pk): # Shows profile
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(pk=pk)
    context = { 'user': user, 'profile': profile }
    return render(request, 'crud/profile.html', context)

class ProfileCreate(CreateView): # Adds profile
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileUpdate(UpdateView): # Updates profile
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileDelete(DeleteView): # Deletes profile
    model = User
    success_url = reverse_lazy('crud:index')
'''
class LoginForm(request):
    model = User
    fields = ['email', 'password']
'''

def logout_view(request): # Logs out user
    logout(request)
    return redirect('crud:index')
