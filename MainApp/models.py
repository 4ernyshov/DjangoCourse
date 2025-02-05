from django.db import models

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    note = models.CharField(max_length=100, default='')

