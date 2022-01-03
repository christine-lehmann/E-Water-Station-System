from rest_framework import serializers
from EWater_api.models import ClientData

class ClientData_Serializer(serializers.ModelSerializer):
 
    class Meta:
        model = ClientData
        fields = ('id',
                  'phone',
                  'fullname',
                  'address',
                  'email',
                  'reservation')