from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=2, decimal_places=5)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, default='text')
    cost = models.DecimalField(max_digits=2,decimal_places=5)
    size = models.DecimalField(max_digits=2,decimal_places=5)
    description = models.TextField(default='text')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
