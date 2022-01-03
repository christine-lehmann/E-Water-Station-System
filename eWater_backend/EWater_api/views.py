from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from EWater_api.models import ClientData
from EWater_api.serializers import ClientData_Serializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    if request.method == 'GET':
            client = ClientData.objects.all()
            
            title = request.GET.get('title', None)
            if title is not None:
                client = client.filter(title__icontains=title)
            
            clientdata_serializer = ClientData_Serializer(client, many=True)
            return JsonResponse(clientdata_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ClientData_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = ClientData.objects.all().delete()
        return JsonResponse({'message': '{} client were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def client_info(request, pk):
    
    try: 
        client = ClientData.objects.get(pk=pk) 
    except ClientData.DoesNotExist: 
        return JsonResponse({'message': 'The ClientData does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        tutorial_serializer = ClientData_Serializer(client) 
        return JsonResponse(tutorial_serializer.data) 
    
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ClientData_Serializer(client, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        client.delete() 
        return JsonResponse({'message': 'ClientData was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        count = client.objects.all().delete()
        return JsonResponse({'message': '{} client were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
    # GET / PUT / DELETE ClientData
