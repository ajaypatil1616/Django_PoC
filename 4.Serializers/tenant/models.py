from django.db import models

class Tenant(models.Model):
    
    name = models.CharField(max_length= 255, null=False)
    age = models.CharField(null=False)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length= 10)
    payment = models.DecimalField(max_digits=60, decimal_places= 4)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)