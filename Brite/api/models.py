from django.db import models 
from django.contrib.auth.models import User

# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name




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





class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    LEAVE_CHOICES = [
        ('annual', 'Annual'),
        ('sick', 'Sick'),
        ('casual', 'Casual'),
    ]    

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='employee'
    )
    leave_type = models.CharField(
        choices=LEAVE_CHOICES,
        default='annual',
        )
    start_date = models.DateField()
    end_date = models.DateField()
    status  = models.CharField(
        choices=STATUS_CHOICES,
        default='pending',
        )
    
    def __str__(self):
        return self.employee +' '+self.leave_type

