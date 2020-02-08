from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Car
from rest_framework import viewsets
from .serializers import CarSerializer

# Create your views here.
"""
class Another(View):

    cars = Car.objects.all()#get cars
    #cars = Car.objects.filter(is_published=True)#filters with this condition

    #output = f"current Book, there are {len(cars)} of data exist"
    output = ''

    for car in cars:
        output += f"Car name: {car.name}, price: {car.price}<br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    cars = Car.objects.all()
    return render(request, 'first_temp.html', {'cars': cars})
"""

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()