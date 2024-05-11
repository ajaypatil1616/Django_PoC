from django.db import models

class Course(models.Model):
    name = models.CharField(max_length= 255)
    code = models.CharField(max_length= 255)

class Student(models.Model):
    name = models.CharField(max_length= 255)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course)