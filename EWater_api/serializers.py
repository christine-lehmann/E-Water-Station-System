from rest_framework import serializers
from EWater_api.models import ClientData, Order_stats_sales, OrderData, OrderStatus
 
 
class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ClientData
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'email')

class OrderDataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = OrderData
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'email',
                  'item',
                  'quantity',
                  'payment',
                  'reservationDate',)

class OrderStatusSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = OrderStatus
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'email',
                  'item',
                  'quantity',
                  'payment',
                  'status',
                  'DateAccepted')

class OrderStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_stats_sales
        fields = ('id',
                  'item',
                  'price',
                  'date')