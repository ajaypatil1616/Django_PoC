from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(models.Model):
    name = models.CharField(max_length= 255, null= False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length= 255)
    age = models.IntegerField()
    number = models.CharField(max_length= 10)
    
class Student(models.Model):
    
    name = models.CharField(max_length= 255, null= False)
    email = models.EmailField(null=False, unique=True)
    roll_no = models.IntegerField(null= False)
    marks = models.BigIntegerField(null= False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    
