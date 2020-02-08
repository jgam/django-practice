# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(blank=False, null=True, unique=True, max_length = 36)
    description = models.TextField(max_length=256, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2)
    published = models.DateField()
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/')
