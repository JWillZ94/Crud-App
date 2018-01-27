from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    image = models.ImageField()
    bio = models.TextField()
    gender = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('crud:profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name
