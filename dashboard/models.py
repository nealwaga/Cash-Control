from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from unicodedata import category

# Create your models here.
class Categories (models.Model):
    catrgory = models.CharField(max_length=25)

    def __str__(self):
        return self.category 


class Expenses(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    category = models.ForeignKey (Categories, on_delete=models.CASCADE)
    description = models.CharField (max_length=50)
    amount =  models.IntegerField (default=0)
    date = models.DateTimeField (auto_now_add=True, null=True)

    def __str__(self):
        return self.description

    @classmethod
    def search_by_description(cls, search_term):
        captions = cls.objects.filter(description_icontains=search_term)
        return captions