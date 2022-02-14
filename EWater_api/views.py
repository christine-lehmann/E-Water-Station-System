import random
from django.shortcuts import redirect, render

from django.http.response import JsonResponse
from django.template import context
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
                client_object = ClientData.objects.filter(phone__icontains=phone)
            
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


############# Start of Orderslip session saver #######################################

def client_info_builder(request):

    fullname = request.POST.get('fullname')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    reservation = request.POST.get('reservation')
    context = {'fullname':fullname,'address':address,'phone':phone,'email':email,'reservation':reservation}
    
    return render(request, 'order.html', context=context)


############### END of Orderslip session saver ####################################


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
            orders_serializer.save(item_id=random.randint(1,500))
            ctx = {
                'id': orders_serializer.data.get('item_id'),
                'fullname': orders_serializer.data.get('fullname'),
                'address': orders_serializer.data.get('address'),
                'phone': orders_serializer.data.get('phone'),
                'email': orders_serializer.data.get('email'),
                'item': orders_serializer.data.get('item'),
                'quantity': orders_serializer.data.get('quantity'),
                'price': orders_serializer.data.get('payment'),
            }
            message = get_template("email/email_order_confirm.html").render(ctx)
            mail = EmailMessage(
                subject="Order Confirmation",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[orders_serializer.data.get("email"),],
            )
            mail.content_subtype = "html"
            mail.send()

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

############### START OF ORDER Status VIEW ####################################

from django.core.mail import EmailMessage
from .models import OrderStatus
from .serializers import OrderStatusSerializer
from django.template.loader import get_template

@api_view(['GET', 'POST', 'DELETE'])
def order_status_list(request):
    if request.method == 'GET':
            Order_object = OrderStatus.objects.all()
            phone = request.GET.get('phone', None)
            if phone is not None:
                Order_object = OrderStatus.filter(phone__icontains=phone)
            order_serializer = OrderStatusSerializer(Order_object, many=True)
            return JsonResponse(order_serializer.data, safe=False)

    elif request.method == 'POST':
        document = JSONParser().parse(request)
        orders_serializer = OrderStatusSerializer(data=document)
        if orders_serializer.is_valid():
            orders_serializer.save()
            status_item = orders_serializer.data.get('status')
            ctx = {
                'id': orders_serializer.data.get('item_id'),
                'fullname': orders_serializer.data.get('fullname'),
                'address': orders_serializer.data.get('address'),
                'phone': orders_serializer.data.get('phone'),
                'email': orders_serializer.data.get('email'),
                'item': orders_serializer.data.get('item'),
                'quantity': orders_serializer.data.get('quantity'),
                'price': orders_serializer.data.get('payment'),
            }
            if status_item == "Deployed":
                message = get_template("email/email_order_ship.html").render(ctx)
                mail = EmailMessage(
                    subject="Delivery in progress",
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[orders_serializer.data.get("email"),],
                )
                mail.content_subtype = "html"
                mail.send()
                
            ## if false 
            message = get_template("email/email_order_accepted.html").render(ctx)
            mail = EmailMessage(
                    subject="Confirmed order",
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[orders_serializer.data.get("email"),],
                )
            mail.content_subtype = "html"
            mail.send()
            
            return JsonResponse(orders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = OrderStatus.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def order_status_detail(request, pk):
    
    try: 
        orders = OrderStatus.objects.get(pk=pk) 
    except OrderStatus.DoesNotExist: 
        return JsonResponse({'message': 'The orders does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        orders_serializer = OrderStatusSerializer(orders) 
        return JsonResponse(orders_serializer.data) 
    
    elif request.method == 'PUT': 
        document = JSONParser().parse(request) 
        orders_serializer = OrderStatusSerializer(orders, data=document) 
        if orders_serializer.is_valid(): 
            orders_serializer.save() 
            return JsonResponse(orders_serializer.data) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        document = JSONParser().parse(request)
        orders_serializer = OrderStatusSerializer(orders, data=document)
        #########
        ctx = {
                'id': orders_serializer.data.get('id'),
                'fullname': orders_serializer.data.get('fullname'),
                'address': orders_serializer.data.get('address'),
                'phone': orders_serializer.data.get('phone'),
                'email': orders_serializer.data.get('email'),
                'item': orders_serializer.data.get('item'),
                'quantity': orders_serializer.data.get('quantity'),
                'price': orders_serializer.data.get('payment'),
        }
        message = get_template("email/email_order_declined.html").render(ctx)
        mail = EmailMessage(
        subject="Order declined",
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[orders_serializer.data.get("email"),],
            )
        mail.content_subtype = "html"
        mail.send()

        orders.delete() 
        return JsonResponse({'message': 'orders was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        count = OrderStatus.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

############### END OF ORDER Status VIEW ####################################

############### START OF ORDER Statistics VIEW ####################################

from .models import Order_stats_sales # Order_stats_sales
from .serializers import OrderStatsSerializer # OrderStatsSerializer
from django.conf import settings
from django.core.mail import send_mail

@api_view(['GET', 'POST', 'DELETE'])
def order_stats_list(request):
    if request.method == 'GET':
            Order_object = Order_stats_sales.objects.all()
            
            phone = request.GET.get('phone', None)
            if phone is not None:
                Order_object = Order_stats_sales.filter(phone__icontains=phone)
            
            order_serializer = OrderStatsSerializer(Order_object, many=True)
            return JsonResponse(order_serializer.data, safe=False)

    elif request.method == 'POST':
        document = JSONParser().parse(request)
        orders_serializer = OrderStatsSerializer(data=document)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse(orders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = Order_stats_sales.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def order_stats_detail(request, pk):
    
    try: 
        orders = Order_stats_sales.objects.get(pk=pk) 
    except Order_stats_sales.DoesNotExist: 
        return JsonResponse({'message': 'The orders does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        orders_serializer = OrderStatsSerializer(orders) 
        return JsonResponse(orders_serializer.data) 
    
    elif request.method == 'PUT': 
        document = JSONParser().parse(request) 
        orders_serializer = OrderStatsSerializer(orders, data=document) 
        if orders_serializer.is_valid(): 
            orders_serializer.save() 
            return JsonResponse(orders_serializer.data) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        orders.delete() 
        return JsonResponse({'message': 'orders was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        count = Order_stats_sales.objects.all().delete()
        return JsonResponse({'message': '{} Order_object were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

############### END OF ORDER Stats VIEW ####################################