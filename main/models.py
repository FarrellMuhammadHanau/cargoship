from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField()
