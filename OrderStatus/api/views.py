from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from OrderStatus.api.serializers import OrderRegisterSerializer, NumberOrderSerializer
from OrderStatus.models import OrderItems, OrderStatus


class OrderApiViewSet(APIView):

    def get(self, request, format=None, *args, **kwargs):
        items=OrderItems.objects.all()
        serializer = OrderRegisterSerializer(items, many=True)
        return Response(serializer.data)


class OrderNumberApiviewSet(APIView):

    def get(self, request, format=None, *args, **kwargs):
        orders = OrderStatus.objects.all()
        test=OrderItems.objects.all()

        for order in orders:
            id = order.OrderNumber
            itemsId = OrderItems.objects.filter(OrderNumber=id)
            pending = 0
            canceled = 0
            itemsLen = len(itemsId)

            for item in itemsId:
                if item.status == 'PENDING':
                    pending +=1
                elif item.status == 'CANCELLED':
                    canceled +=1

            if pending>0:
                order.status = 'PENDING'
            elif canceled == itemsLen:
                order.status= 'CANCELLED'
            else:
                order.status = 'SHIPPED'
        serializer = NumberOrderSerializer(orders, many=True)
        return Response(serializer.data)




