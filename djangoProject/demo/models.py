# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CarNumber(models.Model):
    carnumber = models.CharField(max_length=10, blank=True, null=True)
    carregistrationnumber = models.CharField(max_length=20, blank=True, null=True)

class Car(models.Model):
    name = models.CharField(blank=False, null=True, unique=True, max_length = 36)
    description = models.TextField(max_length=256, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    published = models.DateField(null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    number = models.OneToOneField(
        CarNumber, null=True, blank=True, on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

class Wheels(models.Model):
    name = models.CharField(max_length=30)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='wheels')

class Owner(models.Model):
    name = models.CharField(max_length=30)
    surnawme = models.CharField(max_length=30)
    cars = models.ManyToManyField(Car)