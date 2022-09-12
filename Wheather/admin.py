from django.contrib import admin
from Wheather.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'rain']