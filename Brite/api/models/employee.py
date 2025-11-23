from django.db import models 
from django.contrib.auth.models import User

from .company import Company
# Create your models here.





class Employee(models.Model):

    ROLE_CHOICES = [
        ('hr', 'HR'),
        ('finance', 'Finance'),
        ('engineering', 'Engineering'),
        ('other', 'Other'),
    ]
    user_name =models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company'
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        default = 'other' 
    )
    email = models.EmailField(unique=True)
    joining_date = models.DateField(null=True , blank=True)




    def __str__(self):
        return self.email



