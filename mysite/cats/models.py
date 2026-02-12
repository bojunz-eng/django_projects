 
from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    weight = models.FloatField()
    
    def __str__(self):
        return self.nickname

