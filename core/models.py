from django.db import models
# Create your models here.

class DataBase(models.Model):
    input1 = models.CharField(max_length=50)
    input2 = models.CharField(max_length=50)



    

