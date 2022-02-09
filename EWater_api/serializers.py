from rest_framework import serializers
from EWater_api.models import ClientData, OrderData
 
 
class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ClientData
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'email',
                  'verified')

class OrderDataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = OrderData
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'item',
                  'pendingPayment',
                  'Paid',
                  'Delivered',
                  'reservationDate')