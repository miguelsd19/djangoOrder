from django.db import models


class OrderStatus(models.Model):
    choice = (('SHIPPED', 'SHIPPED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED'))
    OrderNumber = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255, choices=choice)

    def __str__(self):
        return self.OrderNumber


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    choice = (('SHIPPED', 'SHIPPED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED'))
    itemName = models.CharField(max_length=255)
    OrderNumber = models.ForeignKey(OrderStatus, related_name='items', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=choice)

    def __str__(self):
        return self.status





