from django.db import models

# Create your models here.
class user(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email  = models.EmailField(max_length=50)
    Contact=models.BigIntegerField()
    Password=models.CharField(max_length=50)