from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction

def index(request):
    context = {}
    return render(request, 'crud/index.html', context)

@transaction.atomic # If everything runs smooth, it will allow changes to the database
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully created!')
            user = authenticate(request, username=username, password=password2)
            if user is not None:
                login(request, user)
                profile = profile_form.save(commit=False)
                profile.user_id = request.user
                profile.save()
                return redirect('crud:profile', pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'crud/registration_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crud:profile', pk=request.user.pk)
        else:
            messages.error(request, 'Username and/or password do not match.')
    else:
        login_form = LoginForm()
    return render(request, 'crud/login_form.html', { 'login_form': login_form })

@login_required
def profile(request, pk):
    user = User.objects.get(pk=request.user.pk)
    profile = Profile.objects.get(pk=pk)
    context = { 'user': user, 'profile': profile }
    return render(request, 'crud/profile.html', context)

@login_required
@transaction.atomic
def update_profile(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user = authenticate(request, username=username, password=password2)
            if user is not None:
                login(request, user)
                profile = profile_form.save(commit=False)
                profile.user_id = request.user
                profile.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('crud:profile', pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'crud/registration_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class ProfileDelete(DeleteView):
    model = User
    success_url = reverse_lazy('crud:index')

def logout_view(request):
    logout(request)
    messages.success(request, "You are now logged out.")
    return redirect('crud:index')
