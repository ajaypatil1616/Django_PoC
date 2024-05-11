from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    def save(self, *args, **kwargs):
        if self.password :
            self.set_password(self.password)
        super().save(*args, **kwargs)

   

class Employee(models.Model):
    manager = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)    
    age = models.IntegerField()
    username = models.CharField(max_length= 255, default= "ajay1616")
    password = models.CharField(max_length= 255, default="Asdfghjkl123")

