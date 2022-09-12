from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from OrderStatus.models import OrderItems, OrderStatus
from OrderStatus.api.serializers import OrderRegisterSerializer, NumberOrderSerializer
from django.db.models import Q
from OrderStatus.models import OrderItems, OrderStatus
from django.http import JsonResponse


class OrderApiViewSet(ModelViewSet):
    serializer_class = OrderRegisterSerializer
    queryset = OrderItems.objects.all()



class OrderNumberApiviewSet(ModelViewSet):
    #queryset = OrderItems.objects.raw('SELECT')
    serializer_class = NumberOrderSerializer
    queryset = OrderStatus.objects.all()



