from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    Women = 'W'


    desginations_choice = [
        ( Women,'Women'),
    ]
    designation = models.CharField(max_length=1,choices=desginations_choice,default=Women)
    phone = models.CharField(max_length=10,null=True,blank=True)
    db_table = 'User'
   
    def __str__(self):
        return self.username

 
class Caterer(models.Model):
    community_name=models.CharField(max_length=255)
    phoneno=models.CharField(max_length=10)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contract_period=models.IntegerField(max_length=2)
