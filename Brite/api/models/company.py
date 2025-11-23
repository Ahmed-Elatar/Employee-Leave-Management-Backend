from django.db import models 
from django.contrib.auth.models import User

# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name

