from urllib import response
from rest_framework.views import status, APIView
from rest_framework.response import Response
from season.models import Season
from season.api.serializers import GetSeasonSerializer


class seasonView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        season=Season.objects.all()
        for seas in season:
            print(seas.date)
            dt = seas.date.timetuple().tm_yday
            #dt= str(seas.date)
            #dt=dt.split("-")
            spring = range(78,167)
            summer = range(168, 264)
            fall = range(265, 354)
            if dt in spring:
                seas.season ='Spring'
            elif dt in summer:
                seas.season = 'Summer'
            elif dt in fall:
                seas.season = 'Fall'
            else:
                seas.season = 'Winter'

        serializer = GetSeasonSerializer(season, many=True)

        return Response(serializer.data)
