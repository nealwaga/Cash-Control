from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='profile')
    image = CloudinaryField ('image')
    name = models.CharField (blank=False, max_length=100)
    bio = models.CharField (blank=True, max_length=65)
    email = models.EmailField (blank=False, max_length=100)
    income = models.IntegerField (default=0)


    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f'{self.user.username} Profile'

    def __str__(self):
        return self.user


    @receiver (post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver (post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()