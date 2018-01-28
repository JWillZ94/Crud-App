from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Profile
#from .forms import RegisterForm, ProfileForm, LoginForm
from django.urls import reverse_lazy

def index(request):
    context = {}
    return render(request, 'crud/index.html', context)

'''def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('crud:login')

    else:
        form = RegistrationForm()
        profile_form = ProfileForm()


    return render(request, 'crud/registration_form.html', {'form': form})

class ProfileView(generic.DetailView):
    model = User
    template_name = 'crud/user_profile.html'

class ProfileCreate(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileDelete(DeleteView):
    model = User
    success_url = reverse_lazy('crud:index')

class ProfileFormView(View):
    form_class = ProfileForm
    template_name = 'crud/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('crud:profile-add')

        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'crud/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('crud:profile')

def logout_view(request):
    logout(request)
    return redirect('crud:index')

def update_profile(request):
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
    return render(request, 'crud/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
'''
