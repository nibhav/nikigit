from django.db import models

# Create your models here.

class become_dealer(models.Model):
    full_name = models.CharField(max_length=50,null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    city = models.EmailField(max_length=50)
    proposed_firm = models.CharField(max_length=50)
    gst_no = models.EmailField(max_length=50)
    account_number = models.CharField(max_length=20,)
    ifsc_code = models.CharField(max_length=20,)
    account_holder = models.CharField(max_length=20,)

    
