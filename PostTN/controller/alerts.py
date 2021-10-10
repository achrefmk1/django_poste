import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from PostTN.models import Alerts, Systems, Agence, User, Notification, UserProfile
from PostTN.serializer import AlertSerializer, NotificationSerializer
from rest_framework import permissions
from rest_framework.views import APIView


class GetAlerts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request ,id=0):
        if request.method=='GET':
            if id > 0 :
                alert = Alerts.objects.get(id=id)
                alert_serializer = AlertSerializer(alert, many=False)
                return JsonResponse(alert_serializer.data, safe=False)
            else :
                alerts = Alerts.objects.all()
                alert_serializer = AlertSerializer(alerts ,many=True)
                return JsonResponse(alert_serializer.data ,safe=False)


class StoreAlerts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            alert_data = JSONParser().parse(request)
            alert_serializer = AlertSerializer(data=alert_data)
            if alert_serializer.is_valid():
                alert_serializer.save()
                return JsonResponse(alert_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(alert_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateAlerts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def put(self, request ,id):
        if request.method=='PUT':
            alert_data =JSONParser().parse(request)
            alert =Alerts.objects.get(id=id)
            alert_serializer =AlertSerializer(alert ,data=alert_data)
            if alert_serializer.is_valid():
                alert_serializer.save()
                return JsonResponse("Updated Successfully" ,safe=False)
            return JsonResponse("Failed to Update")


class DeleteAlerts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def delete(self, request ,id):
        if request.method == 'DELETE':
            alert = Alerts.objects.get(id=id)
            alert.delete()
            return JsonResponse("Deleted Successfully", safe=False)


class SaveNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request, agence, system, alert):
        if request.method == 'GET':
            alert = Alerts.objects.get(id=alert)
            agence = Agence.objects.get(id=agence)
            system = Systems.objects.get(id=system)
            data = {
                'agence': agence.id,
                'system': system.id,
                'alert': alert.id,
                'message': alert.text,
                'alertDate': datetime.datetime.now(),
                'fixedDate': datetime.datetime.now(),
                'user': agence.userID.id,
                'status': 0
            }
            notification_serializer = NotificationSerializer(data=data)
            if notification_serializer.is_valid():
                notification_serializer.save()
                return JsonResponse("saved Successfully", safe=False)
            return JsonResponse(notification_serializer.errors, safe=False)


class GetUserNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        if request.method == 'GET':
            user = User.objects.get(username=request.user)
            profile = UserProfile.objects.get(user=user.id)
            notifications = []
            if profile.is_chef == 'yes':
                agencesList = Agence.objects.filter(city=profile.work_area)
                for agence in agencesList:
                    notificationsList = agence.notification_set.all()
                    for notification in notificationsList:
                        item = {
                            'id': notification.id,
                            'text': notification.message,
                            'date': notification.alertDate.strftime('%m/%d/%Y %H:%M:%S'),
                            'system': notification.system.name,
                            'systemID': notification.system.id,
                            'status': notification.status,
                            'type': notification.alert.type
                        }
                        notifications = notifications + [item]
                return HttpResponse(json.dumps(notifications))

            notificationsList = user.notification_set.all()
            for notification in notificationsList:
                item = {
                    'id': notification.id,
                    'text': notification.message,
                    'date': notification.alertDate.strftime('%m/%d/%Y %H:%M:%S'),
                    'system': notification.system.name,
                    'systemID': notification.system.id,
                    'status': notification.status,
                    'type': notification.alert.type
                }
                notifications = notifications + [item]
            return HttpResponse(json.dumps(notifications))


class UpdateNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request,id,status):
        if request.method == 'GET':
            notification = Notification.objects.get(id=id)
            if status == '2':
                notification.fixedDate = datetime.datetime.now()
            notification.status = status
            notification.save()
            return JsonResponse('updated', safe=False)


class GetAllNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        if request.method == 'GET':
            notifications = []
            agencesList = Agence.objects.all()
            for agence in agencesList:
                notificationsList = agence.notification_set.all()
                for notification in notificationsList:
                    item = {
                        'id': notification.id,
                        'text': notification.message,
                        'date': notification.alertDate.strftime('%m/%d/%Y %H:%M:%S'),
                        'system': notification.system.name,
                        'user': notification.user.first_name,
                        'matricule': notification.user.username,
                        'systemID': notification.system.id,
                        'status': notification.status,
                        'type': notification.alert.type,
                        'agence': agence.name
                    }
                    notifications = notifications + [item]
            return HttpResponse(json.dumps(notifications))
