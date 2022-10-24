from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    image = CloudinaryField ('image')
    name = models.CharField (blank=False, max_length=100)
    bio = models.CharField (blank=True, max_length=65)
    email = models.EmailField (blank=False, max_length=100)
    income = models.IntegerField (default=0)