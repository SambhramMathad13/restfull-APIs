from rest_framework import serializers
from .models import Studs

class Studserializer(serializers.ModelSerializer):
    class Meta:
        model = Studs
        fields = ['id', 'name', 'roll']