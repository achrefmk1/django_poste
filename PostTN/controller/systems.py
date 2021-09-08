from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.core import serializers

from rest_framework.decorators import api_view
from PostTN.models import Systems
from PostTN.serializer import SystemSerializer

from rest_framework import permissions
from rest_framework.views import APIView


class GetSystem(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request , id=0):
        if request.method == 'GET':
            if id > 0:
                systems = Systems.objects.get(id=id)
                system_serializer = SystemSerializer(systems ,many=False)
                return JsonResponse(system_serializer.data ,safe=False)
            else :
                systems = Systems.objects.all()
                system_serializer = SystemSerializer(systems ,many=True)
                return JsonResponse(system_serializer.data ,safe=False)


class StoreSystem(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            system_data = JSONParser().parse(request)
            system_serializer = SystemSerializer(data=system_data)
            if system_serializer.is_valid():
                system_serializer.save()
                return JsonResponse(system_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(system_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSystem(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def put(self, request ,id):
        if request.method=='PUT':
            system_data =JSONParser().parse(request)
            system =Systems.objects.get(id=id)
            system_serializer =SystemSerializer(system ,data=system_data)
            if system_serializer.is_valid():
                system_serializer.save()
                return JsonResponse(system_serializer.data)
            return JsonResponse(system_serializer.errors)


class DeleteSystem(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def delete(self, request ,id):
        if request.method == 'DELETE':
            system = Systems.objects.get(id=id)
            system.delete()
            return JsonResponse("Deleted Successfully", safe=False)


class GetSystemAlerts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request, id):
        if request.method == 'GET':
            system = Systems.objects.get(id=id)
            alertsList = []
            for alert in system.alerts_set.all():
                item = {
                    'id': alert.id,
                    'text': alert.text,
                }
                alertsList = alertsList + [item]
            return JsonResponse(alertsList, safe=False)

