from django.urls import path
from OrderStatus.api.views import OrderApiViewSet, OrderNumberApiviewSet


urlpatterns = [
    path('Orders', OrderApiViewSet.as_view(), name='OrderApiViewSet'),
    path('OrderStatus', OrderNumberApiviewSet.as_view(), name='OrderNumberApiViewSet')

]
