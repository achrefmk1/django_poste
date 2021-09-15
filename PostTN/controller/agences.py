from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
import json

from rest_framework.decorators import api_view
from PostTN.models import Agence, Cities, Systems, Alerts
from PostTN.serializer import AgenceSerializer, CitiesSerializer, AgenceSystemsSerializer


from rest_framework import permissions
from rest_framework.views import APIView


class GetAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request ,id=0):
        if request.method=='GET':
            if id > 0 :
                agence = Agence.objects.get(id=id)
                agence_serializer = AgenceSerializer(agence, many=False)
                return JsonResponse(agence_serializer.data, safe=False)
            else:
                # agence = Agence.objects.all()
                # agence_serializer =AgenceSerializer(agence ,many=True)
                # return JsonResponse(agence_serializer.data ,safe=False)
                agences = Agence.objects.all()
                users = []

                for agence in agences:
                    item = {
                        'id': agence.id,
                        'name': agence.name,
                        'address': agence.address,
                        'city': agence.city,
                        'username': agence.userID.username,
                        'userID': agence.userID.id}
                    users = users + [item]
                return HttpResponse(json.dumps(users), content_type="application/json")


class StoreAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            agence_data = JSONParser().parse(request)
            agence_serializer = AgenceSerializer(data=agence_data)
            if agence_serializer.is_valid():
                agence_serializer.save()
                return JsonResponse("Saved Successfully", safe=False)
            return JsonResponse(agence_serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class UpdateAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def put(self, request ,id):
        if request.method=='PUT':
            agence_data =JSONParser().parse(request)
            agence =Agence.objects.get(id=id)
            agence_serializer =AgenceSerializer(agence ,data=agence_data)
            if agence_serializer.is_valid():
                agence_serializer.save()
                return JsonResponse("Updated Successfully" ,safe=False)
            return JsonResponse(agence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def delete(self, request ,id):
        if request.method == 'DELETE':
            agence = Agence.objects.get(id=id)
            agence.delete()
            return JsonResponse("Deleted Successfully", safe=False)


class GetCities(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        cities = Cities.objects.all()
        cities_serializer = CitiesSerializer(cities, many=True)
        return JsonResponse(cities_serializer.data, safe=False)


class GetSystemsAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        agences = Agence.objects.all()
        agencesList = []
        for agence in agences:
            systems = []
            for system in agence.systems_set.all():
                item = {
                    'id': system.id,
                    'name': system.name,
                }
                systems = systems + [item]
            if len(systems) > 0:
                item = {
                    'id': agence.id,
                    'name': agence.name,
                    'systems': systems
                }
                agencesList = agencesList + [item]
        return JsonResponse(agencesList, safe=False)


class AffectSystemToAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request , systemId, agenceId):
        if request.method == 'GET':
            system = Systems.objects.get(id=systemId)
            agence = Agence.objects.get(id=agenceId)
            system.agences.add(agence)
            return JsonResponse("saved Successfully", safe=False)


class getSystemsByAgenceID(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request , agenceId):
        if request.method == 'GET':
            agence = Agence.objects.get(id=agenceId)
            systems = []
            for system in agence.systems_set.all():
                item = {
                    'id': system.id,
                    'name': system.name,
                }
                systems = systems + [item]
            return JsonResponse(systems, safe=False)


class removeSystemsByAgenceID(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def delete(self, request , agenceId, systemId):
        if request.method == 'DELETE':
            system = Systems.objects.get(id=systemId)
            agence = Agence.objects.get(id=agenceId)
            system.agences.remove(agence)
            return JsonResponse('deleted', safe=False)
