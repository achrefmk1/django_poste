from rest_framework import serializers
from PostTN.models import Agence,Users,Systems,Alerts


class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields=('id','name','address')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','name','email','phone','matricule','password','is_chef')


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Systems
        fields=('id','name')


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alerts
        fields=('id','type','text','chef_only','systemID')