from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    age = models.IntegerField()
    object_buyer = models.Manager()
    DoesNotExist = models.Manager

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, default='text')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='text')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
