from django.contrib import admin
from OrderStatus.models import OrderItems, OrderStatus


@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['OrderNumber', 'status']

@admin.register(OrderItems)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['OrderNumber', 'itemName', 'status']
