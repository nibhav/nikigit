from django.db import models


# Create your models here.

class car(models.Model):
    title =models.CharField( max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(max_length=None)