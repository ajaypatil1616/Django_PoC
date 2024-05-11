from django.db import models

class Owner(models.Model):
    
    name = models.CharField(max_length= 255,null= False )
    age = models.CharField(null= False)
    email = models.EmailField(unique= True)
    number = models.CharField(max_length=10, null= False, unique= True)
    wing = models.CharField(max_length= 100, null= False, default= 'D')
    flat_no = models.IntegerField(null= False, unique=True)
    
class Ten(models.Model):
    
    t_name = models.CharField(max_length= 255,null= False )
    t_age = models.CharField(null= False)
    t_email = models.EmailField(unique= True)
    t_number = models.CharField(max_length=10, null= False, unique= True)
    t_rent = models.BigIntegerField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)

