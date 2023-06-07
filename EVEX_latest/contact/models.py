from django.db import models



# Create your models here.

class form(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    enquiry = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.firstname