from rest_framework import serializers
from season.models import Season


class GetSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'date', 'season']
