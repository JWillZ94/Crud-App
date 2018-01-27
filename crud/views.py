from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm
from .forms import UserForm
from django.urls import reverse_lazy

def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('crud/profile.html')
    else:
        form = ProfileForm()

    return render(request, 'crud/index.html', {'form': form})

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'crud/profile.html'

class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'password', 'email', 'image', 'bio', 'gender']

class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('crud:index')

class UserFormView(View):
    form_class = UserForm
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
