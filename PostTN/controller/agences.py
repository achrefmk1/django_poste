from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from PostTN.models import Agence, Cities, AgenceSystems, Systems, Alerts
from PostTN.serializer import AgenceSerializer, CitiesSerializer, AgenceSystemsSerializer


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


@csrf_exempt
def GetSystemsAgence(request):
    systems = AgenceSystems.objects.all()
    systems_serializer = AgenceSystemsSerializer(systems, many=True)
    return JsonResponse(systems_serializer.data, safe=False)


@csrf_exempt
def AffectSystemToAgence(request , systemId, agenceId):
    if request.method == 'GET':
        system = Systems.objects.get(id=systemId)
        agence = Agence.objects.get(id=agenceId)
        agence_system_serializer = AgenceSystemsSerializer(data={'systemID' : systemId, 'agenceID' : agenceId})
        if agence_system_serializer.is_valid():
            agence_system_serializer.save()
            return JsonResponse("saved Successfully", safe=False)
        return JsonResponse("error", safe=False)


@csrf_exempt
def Notification(request , systemId, agenceId):
    # alertID
    if request.method == 'POST':
        alert = Alerts.objects.get(systemId=systemId)
        agence = Agence.objects.get(id=agenceId)
        agence_system_serializer = AgenceSystemsSerializer(data={'alertID' : alert.id, 'agenceID' : agenceId, 'message' : alert.text})
        if agence_system_serializer.is_valid():
            agence_system_serializer.save()
            return JsonResponse("saved Successfully", safe=False)
        return JsonResponse("error", safe=False)

@csrf_exempt
def getSystemsByAgenceID(request , agenceId):
    if request.method == 'GET':
        agence = Agence.objects.get(id=agenceId)
        return JsonResponse(agence.systemID, safe=False)
        # agence_system_serializer = AgenceSystemsSerializer(data={'alertID' : alert.id, 'agenceID' : agenceId, 'message' : alert.text})
        # if agence_system_serializer.is_valid():
        #     agence_system_serializer.save()
        #     return JsonResponse("saved Successfully", safe=False)
        return JsonResponse("error", safe=False)

