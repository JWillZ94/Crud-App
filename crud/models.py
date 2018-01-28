from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    GENDER = (
        ('I do not wish to specify.', 'I do not wish to specify.'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    '''first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)'''
    image = models.ImageField()
    bio = models.TextField()
    gender = models.CharField(max_length=20, choices = GENDER)

    def get_absolute_url(self):
        return reverse('crud:profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
