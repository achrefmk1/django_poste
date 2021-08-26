from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from PostTN.models import Agence,Cities
from PostTN.serializer import AgenceSerializer,CitiesSerializer


@csrf_exempt
def GetAgence(request ,id=0):
    if request.method=='GET':
        if id > 0 :
            agence = Agence.objects.get(id=id)
            agence_serializer = AgenceSerializer(agence, many=False)
            return JsonResponse(agence_serializer.data, safe=False)
        else:
            agence = Agence.objects.all()
            agence_serializer =AgenceSerializer(agence ,many=True)
            return JsonResponse(agence_serializer.data ,safe=False)

@csrf_exempt
def StoreAgence(request):
    if request.method == 'POST':
        agence_data = JSONParser().parse(request)
        agence_serializer = AgenceSerializer(data=agence_data)
        if agence_serializer.is_valid():
            agence_serializer.save()
            return JsonResponse(agence_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(agence_serializer, status=status.HTTP_400_BAD_REQUEST, safe=False)

@csrf_exempt
def UpdateAgence(request ,id):
    if request.method=='PUT':
        agence_data =JSONParser().parse(request)
        agence =Agence.objects.get(id=id)
        agence_serializer =AgenceSerializer(agence ,data=agence_data)
        if agence_serializer.is_valid():
            agence_serializer.save()
            return JsonResponse("Updated Successfully" ,safe=False)
        return JsonResponse(agence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def DeleteAgence(request ,id):
    if request.method == 'DELETE':
        agence = Agence.objects.get(id=id)
        agence.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def GetCities(request):
    cities = Cities.objects.all()
    cities_serializer = CitiesSerializer(cities, many=True)
    return JsonResponse(cities_serializer.data, safe=False)


