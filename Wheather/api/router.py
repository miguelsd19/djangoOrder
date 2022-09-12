from django.urls import path
from Wheather.api.views import WeatherView, AllDayWeatherView


urlpatterns = [
    path('Weather', WeatherView.as_view(), name='WeatherView'),
    path('AllDaysWeather', AllDayWeatherView.as_view(), name='AllDaysWeatherView'),

]