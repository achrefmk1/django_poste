from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from PostTN.models import Systems
from PostTN.serializer import SystemSerializer


@csrf_exempt
def GetSystem(request , id=0):
    if request.method == 'GET':
        if id > 0:
            systems = Systems.objects.get(id=id)
            system_serializer = SystemSerializer(systems ,many=False)
            return JsonResponse(system_serializer.data ,safe=False)
        else :
            systems = Systems.objects.all()
            system_serializer = SystemSerializer(systems ,many=True)
            return JsonResponse(system_serializer.data ,safe=False)


@csrf_exempt
def StoreSystem(request):
    if request.method == 'POST':
        system_data = JSONParser().parse(request)
        system_serializer = SystemSerializer(data=system_data)
        if system_serializer.is_valid():
            system_serializer.save()
            return JsonResponse(system_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(system_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def UpdateSystem(request ,id):
    if request.method=='PUT':
        system_data =JSONParser().parse(request)
        system =Systems.objects.get(id=id)
        system_serializer =SystemSerializer(system ,data=system_data)
        if system_serializer.is_valid():
            system_serializer.save()
            return JsonResponse("Updated Successfully" ,safe=False)
        return JsonResponse("Failed to Update")
@csrf_exempt
def DeleteSystem(request ,id):
    if request.method == 'DELETE':
        system = Systems.objects.get(id=id)
        system.delete()
        return JsonResponse("Deleted Successfully", safe=False)
