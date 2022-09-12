from rest_framework.views import status, APIView
from rest_framework.response import Response
from Wheather.models import Weather
from Wheather.api.serializer import RainOrNotSerializer

class WeatherView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        days=Weather.objects.all()
        BadDays=[]
        x=0;
        for i in range(1, len(days)):
            var = days[x].rain
            if (not var) and (days[i].rain == True):
                BadDays.append(days[i])
                x = x + 1
            else:
                x=x+1
        serializer = RainOrNotSerializer(BadDays, many=True)
        return Response(serializer.data)

class AllDayWeatherView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        days = Weather.objects.all()
        serializer = RainOrNotSerializer(days, many=True)
        return Response(serializer.data)
