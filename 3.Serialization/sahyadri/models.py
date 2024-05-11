from django.db import models

class Manager(models.Model):
   
    name = models.CharField(max_length=255)
    email = models.EmailField(unique= True, null= False)
    number = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=4)
    
class Employee(models.Model):
   
    e_name = models.CharField(max_length=255)
    e_dept = models.TextField()
    manager_id = models.ForeignKey(Manager, on_delete= models.CASCADE) #one to many
 