from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)