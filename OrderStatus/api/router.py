from rest_framework.routers import DefaultRouter
from OrderStatus.api.views import OrderApiViewSet, OrderNumberApiviewSet


router_category = DefaultRouter()

router_category.register(prefix='Orders', basename='Orders', viewset=OrderApiViewSet)
router_category.register(prefix='OrderNumber', basename='OrderNumber', viewset=OrderNumberApiviewSet)
