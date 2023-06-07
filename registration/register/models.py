from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class regis(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)