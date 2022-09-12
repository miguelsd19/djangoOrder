from OrderStatus.models import OrderItems, OrderStatus
from rest_framework import serializers
import logging


class OrderRegisterSerializer(serializers.ModelSerializer):
    #items = serializers.RelatedField(many=True, queryset = OrderItems.objects.all())

    class Meta:
        model = OrderItems
        fields = ['itemName', 'OrderNumber', 'status']
        order_by = 'OrderNumber'


class NumberOrderSerializer(serializers.ModelSerializer):
    #test = serializers.CharField(source='OrderItems.status', read_only=True)
    #data= OrderItems.objects.filter(OrderNumber__contains= = '1')
    class Meta:
        model = OrderStatus
        fields = ['OrderNumber', 'status']

