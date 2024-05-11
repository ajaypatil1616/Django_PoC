from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length= 255, null= False)
    email = models.EmailField(null=False, unique=True)
    age = models.IntegerField()
    number = models.CharField(max_length= 10)
    subjects = models.CharField(max_length= 20,default='CNS', choices=(
        ("CNS",'CNS'),
        ("SE",'SE'),
        ("AI",'AI'),
    ))
class Student(models.Model):
    
    name = models.CharField(max_length= 255, null= False)
    email = models.EmailField(null=False, unique=True)
    roll_no = models.IntegerField(null= False)
    marks = models.BigIntegerField(null= False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    
