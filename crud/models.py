from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    bio = models.TextField()
    GENDER = (
        ('I do not wish to specify.', 'I do not wish to specify.'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=30, choices=GENDER)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'image', 'bio', 'gender']
    USERNAME_FIELD = 'user'
    is_anonymous = False
    is_authenticated = False

    class Meta:
        db_table = 'crud_profile'

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

# Creates a profile
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        Profile.objects.create(user=instance)
        profile = Profile(user=user)
        profile.save()
post_save.connect(create_profile, sender=User)

'''
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
'''
# Updates the profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
