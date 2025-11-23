from django.db import models 
from django.contrib.auth.models import User
from .employee import Employee




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

