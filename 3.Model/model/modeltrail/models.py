from django.db import models

class Trails(models.Model):
    first_name = models.CharField(max_length= 35)
    last_name = models.CharField(max_length= 35)
    number = models.BigIntegerField()
    age = models.IntegerField(null= True)
    
