from django.db import models

class RegistrationData(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 255, null= False)
    last_name = models.CharField(max_length= 255, null= False)
    age = models.IntegerField(null= False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length= 32, null= False)
    confirm_password = models.CharField(max_length= 32, null =False)
    number = models.BigIntegerField(null= False)
    gender = models.CharField(max_length= 50, null= False, default= 'M')
    dob = models.DateField(null= False)