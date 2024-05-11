from django.db import models

class Doctor(models.Model):
   
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=4)
    
class Patient(models.Model):
   
    p_name = models.CharField(max_length=255)
    p_disease = models.TextField()
    doctor_id = models.OneToOneField(Doctor, on_delete= models.CASCADE)
 