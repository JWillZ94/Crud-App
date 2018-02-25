from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='', max_length=100)
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

    def get_absolute_url(self):
        return reverse('crud:profile', kwargs={'pk': self.user.pk})

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.pk)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        profile = Profile.objects.get_or_create(user=kwargs.get('instance'))


'''
# Creates a profile
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=request.user)
        profile.save()
post_save.connect(create_profile, sender=User)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Updates the profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
