from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'crud'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.update_profile, name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.profile, name="profile"),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
]


'''
url(r'profile/add/$', views.profile, name='profile-add'),
'''
