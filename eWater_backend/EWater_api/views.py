from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import ClientData, OrderData
from .serializers import ClientSerializer, OrderDataSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    if request.method == 'GET':
            client_object = ClientData.objects.all()
            
            phone = request.GET.get('phone', None)
            if phone is not None:
                client_object = ClientData.filter(phone__icontains=phone)
            
            client_serializer = ClientSerializer(client_object, many=True)
            return JsonResponse(client_serializer.data, safe=False)
    elif request.method == 'POST':
        document = JSONParser().parse(request)
        clients_serializer = ClientSerializer(data=document)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse(clients_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(clients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = ClientData.objects.all().delete()
        return JsonResponse({'message': '{} client_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    
    try: 
        client = ClientData.objects.get(pk=pk) 
    except ClientData.DoesNotExist: 
        return JsonResponse({'message': 'The client does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        clients_serializer = ClientSerializer(client) 
        return JsonResponse(clients_serializer.data) 
    
    elif request.method == 'PUT': 
        document = JSONParser().parse(request) 
        clients_serializer = ClientSerializer(client, data=document) 
        if clients_serializer.is_valid(): 
            clients_serializer.save() 
            return JsonResponse(clients_serializer.data) 
        return JsonResponse(clients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        client.delete() 
        return JsonResponse({'message': 'client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        count = ClientData.objects.all().delete()
        return JsonResponse({'message': '{} client_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET'])
def Client_list_verified(request):
    client_object = ClientData.objects.filter(verified__in=[True])

    if request.method == 'GET':
        client_serializer = ClientSerializer(client_object, many=True)
        return JsonResponse(client_serializer.data, safe=False)

############# END OF CLIENT VIEW #######################################


############### START OF ORDER VIEW ####################################

from .models import OrderData
from .serializers import OrderDataSerializer

@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
            Order_object = OrderData.objects.all()
            
            phone = request.GET.get('phone', None)
            if phone is not None:
                Order_object = OrderData.filter(phone__icontains=phone)
            
            order_serializer = OrderDataSerializer(Order_object, many=True)
            return JsonResponse(order_serializer.data, safe=False)
    elif request.method == 'POST':
        document = JSONParser().parse(request)
        orders_serializer = OrderDataSerializer(data=document)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse(orders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = OrderData.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    
    try: 
        orders = OrderData.objects.get(pk=pk) 
    except OrderData.DoesNotExist: 
        return JsonResponse({'message': 'The orders does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        orders_serializer = OrderDataSerializer(orders) 
        return JsonResponse(orders_serializer.data) 
    
    elif request.method == 'PUT': 
        document = JSONParser().parse(request) 
        orders_serializer = OrderDataSerializer(orders, data=document) 
        if orders_serializer.is_valid(): 
            orders_serializer.save() 
            return JsonResponse(orders_serializer.data) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        orders.delete() 
        return JsonResponse({'message': 'orders was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        count = OrderData.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Order_list_delivered(request):
    Order_object = OrderData.objects.filter(Delivered__in=[False])

    if request.method == 'GET':
        order_serializer = OrderDataSerializer(Order_object, many=True)
        return JsonResponse(order_serializer.data, safe=False)

@api_view(['GET'])
def Order_list_paid(request):
    Order_object = OrderData.objects.filter(Paid__in=[False])

    if request.method == 'GET':
        order_serializer = OrderDataSerializer(Order_object, many=True)
        return JsonResponse(order_serializer.data, safe=False)

############### END OF ORDER VIEW ####################################

