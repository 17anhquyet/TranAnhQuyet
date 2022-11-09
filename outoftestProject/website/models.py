from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=254)
    age = models.PositiveIntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
