from rest_framework import serializers
from Wheather.models import Weather


class RainOrNotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['date', 'rain']
