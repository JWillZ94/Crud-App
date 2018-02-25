from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'crud'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name="profile"),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'profile/(?P<pk>[0-9]+)/update/$', views.update_profile, name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
]
