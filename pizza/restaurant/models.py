from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return (self.name)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    cheese = models.CharField(max_length=30)
    thickness = models.CharField(max_length=20)
    secret = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
