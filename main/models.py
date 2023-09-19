from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()
    weight = models.FloatField()
    container = models.ForeignKey(Container, on_delete=models.CASCADE, default=1)
    description = models.TextField()