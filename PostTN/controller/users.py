from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from PostTN.models import Users
from PostTN.serializer import UserSerializer


@csrf_exempt
def GetUser(request , id=0):
    if request.method == 'GET':
        if id > 0 :
            user = Users.objects.get(id=id)
            user_serializer = UserSerializer(user, many=False)
            return JsonResponse(user_serializer.data, safe=False)
        else:
            user = Users.objects.all()
            user_serializer = UserSerializer(user ,many=True)
            return JsonResponse(user_serializer.data ,safe=False)


@csrf_exempt
def StoreUser(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def UpdateUser(request ,id):
    if request.method=='PUT':
        user_data =JSONParser().parse(request)
        user =Users.objects.get(id=id)
        user_serializer =UserSerializer(user ,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully" ,safe=False)
        return JsonResponse("Failed to Update")
@csrf_exempt
def DeleteUser(request ,id):
    if request.method == 'DELETE':
        user = Users.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
