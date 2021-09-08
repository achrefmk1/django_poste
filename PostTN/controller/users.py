from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from PostTN.models import Agence, UserProfile
from PostTN.serializer import UserSerializer, AgenceUsersSerializer,UserProfileSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class GetUsers(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def get(self, request, id=0):
        if request.method == 'GET':
            if id > 0:
                profile = UserProfile.objects.get(user=id)
                user = {
                    'id': profile.user.id,
                    'name': profile.user.username,
                    'email': profile.user.email,
                    'matricule': profile.matricule,
                    'phone': profile.phone,
                    'is_chef': profile.is_chef,
                    'work_area': profile.work_area}
                return HttpResponse(json.dumps(user), content_type="application/json")
            else:
                profiles = UserProfile.objects.all()
                users = []

                for profile in profiles:
                    item = {
                        'id': profile.user.id,
                        'name': profile.user.username,
                        'email': profile.user.email,
                        'matricule': profile.matricule,
                        'phone': profile.phone,
                        'is_chef': profile.is_chef,
                        'work_area': profile.work_area}
                    users = users + [item]
                return HttpResponse(json.dumps(users), content_type="application/json")


class StoreUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            user = User.objects.create_user(user_data['name'], user_data['email'], user_data['password'])
            user.save()
            profile = UserProfile(matricule=user_data['matricule'], phone=user_data['phone'], is_chef=user_data['is_chef'], work_area=user_data['work_area'], user=user)
            profile.save()
            return JsonResponse('saved susccessfully', safe=False)


class UpdateUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def put(self, request ,id):
        if request.method=='PUT':
            user_data = JSONParser().parse(request)
            u = User.objects.get(id=id)
            u.username = user_data['name']
            u.email = user_data['email']
            u.save()
            profile = UserProfile.objects.get(user=u)
            profile.matricule=user_data['matricule']
            profile.phone=user_data['phone']
            profile.is_chef=user_data['is_chef']
            profile.work_area=user_data['work_area']
            profile.save()
            return JsonResponse("Updated Successfully", safe=False)


class DeleteUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def delete(self, request ,id):
        if request.method == 'DELETE':
            user = User.objects.get(id=id)
            profile = UserProfile.objects.get(user=user)
            profile.delete()
            user.delete()
            return JsonResponse("Deleted Successfully", safe=False)


class AffectUserToAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def get(self, request , userId, agenceId):
        if request.method == 'GET':
            user = User.objects.get(id=userId)
            agence = Agence.objects.get(id=agenceId)
            agence_user_serializer = AgenceUsersSerializer(data={'userID' : userId, 'agenceID' : agenceId})
            if agence_user_serializer.is_valid():
                agence_user_serializer.save()
                return JsonResponse("saved Successfully", safe=False)
            return JsonResponse("error", safe=False)


class GetUserAgence(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        if request.method == 'GET':
            usersagences = User.objects.all()
            agenceuser_serializer = AgenceUsersSerializer(usersagences, many=True)
            return JsonResponse(agenceuser_serializer.data, safe=False)


class GetUserInfo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        if request.method == 'GET':
            auth_user = User.objects.get(username=request.user)
            profile = UserProfile.objects.get(user=auth_user)
            user = {
                'id': profile.user.id,
                'name': profile.user.username,
                'email': profile.user.email,
                'matricule': profile.matricule,
                'phone': profile.phone,
                'is_chef': profile.is_chef,
                'work_area': profile.work_area}
            return HttpResponse(json.dumps(user), content_type="application/json")
