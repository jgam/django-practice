# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Car, CarNumber, Wheels, Owner

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    #fields = ['title', 'description']
    list_display = ['name', 'price']
    list_filter = ['published']
    search_fields = ['name']

# Register your models here.
#admin.site.register(Car)
admin.site.register(CarNumber)
admin.site.register(Wheels)
admin.site.register(Owner)
