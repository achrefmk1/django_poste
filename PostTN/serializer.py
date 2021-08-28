from rest_framework import serializers
from PostTN.models import Agence, Users, Systems, Alerts, AgenceUsers, AgenceSystems, Notification


class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields=('id','name','address','city')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','name','email','phone','matricule','password','is_chef', 'work_area')


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
        model = AgenceUsers
        fields = ('id', 'agenceID', 'userID')


class AgenceSystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenceSystems
        fields = ('id', 'agenceID', 'systemID')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'agenceID', 'systemID', 'message')


