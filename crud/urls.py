from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'crud'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name="profile"),
    url(r'profile/add/$', views.ProfileCreate.as_view(), name='profile-add'),
    url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
]
