from rest_framework import serializers
from .models import Car, CarNumber, Wheels


class CarNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarNumber
        fields = ['id', 'carnumber','carregistrationnumber']

class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheels
        fields = ['id','name']

class CarSerializer(serializers.ModelSerializer):
    number = CarNumberSerializer(many=False)# finds CarNumberSerializer class and populates it
    wheels = WheelSerializer(many=True)
    class Meta:
        model = Car
        fields = ['id', 'name', 'description','price','number','wheels']


