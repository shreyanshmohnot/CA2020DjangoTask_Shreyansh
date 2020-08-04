from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
