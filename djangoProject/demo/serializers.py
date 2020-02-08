from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name'] # 여기에 model field를 추가해주면 된다. 겁나쉽네;