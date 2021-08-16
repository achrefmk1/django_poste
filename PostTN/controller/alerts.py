from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from PostTN.models import Alerts
from PostTN.serializer import AlertSerializer


@csrf_exempt
def GetAlerts(request ,id=0):
    if request.method=='GET':
        if id > 0 :
            alert = Alerts.objects.get(id=id)
            alert_serializer = AlertSerializer(alert, many=False)
            return JsonResponse(alert_serializer.data, safe=False)
        else :
            alerts = Alerts.objects.all()
            alert_serializer = AlertSerializer(alerts ,many=True)
            return JsonResponse(alert_serializer.data ,safe=False)


@csrf_exempt
def StoreAlerts(request):
    if request.method == 'POST':
        alert_data = JSONParser().parse(request)
        alert_serializer = AlertSerializer(data=alert_data)
        if alert_serializer.is_valid():
            alert_serializer.save()
            return JsonResponse(alert_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(alert_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def UpdateAlerts(request ,id):
    if request.method=='PUT':
        alert_data =JSONParser().parse(request)
        alert =Alerts.objects.get(id=id)
        alert_serializer =AlertSerializer(alert ,data=alert_data)
        if alert_serializer.is_valid():
            alert_serializer.save()
            return JsonResponse("Updated Successfully" ,safe=False)
        return JsonResponse("Failed to Update")


@csrf_exempt
def DeleteAlerts(request ,id):
    if request.method == 'DELETE':
        alert = Alerts.objects.get(id=id)
        alert.delete()
        return JsonResponse("Deleted Successfully", safe=False)
