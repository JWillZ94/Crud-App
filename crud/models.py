from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    GENDER = (
        ('I do not wish to specify.', 'I do not wish to specify.'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    bio = models.TextField()
    gender = models.CharField(max_length=20, choices=GENDER)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'image', 'bio', 'gender']
    USERNAME_FIELD = 'user'
    is_anonymous = False
    is_authenticated = False

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
