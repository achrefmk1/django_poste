from rest_framework import serializers
from PostTN.models import Agence, Systems, Alerts, Notification,UserProfile
from django.contrib.auth.models import User


class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = ('id', 'name', 'address', 'city', 'userID')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('phone', 'matricule', 'is_chef', 'work_area', 'userID')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )



class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Systems
        fields=('id','name')


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = ('id', 'type', 'text', 'chef_only', 'systemID')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields=('id','city')


class AgenceUsersSerializer(serializers.ModelSerializer):
    class Meta:
        # model = AgenceUsers
        model = Agence
        fields = ('id', 'agenceID', 'userID')


class AgenceSystemsSerializer(serializers.ModelSerializer):
    systemID = SystemSerializer(read_only=True, many=True)
    class Meta:
        # model = AgenceSystems
        model = Agence
        fields = ('id', 'agenceID', 'systemID')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'agence', 'system', 'alert', 'message', 'alertDate', 'fixedDate', 'user', 'status')


