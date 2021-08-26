# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    matricule = models.IntegerField()
    password = models.CharField(max_length=100)
    is_chef = models.CharField(max_length=50,default='yes')
    work_area = models.CharField(max_length=50)


class Agence (models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)


class AgenceUsers (models.Model):
    agenceID = models.ForeignKey(Agence)
    userID = models.ForeignKey(Users)


class alertType(enumerate):
    warning = "warning"
    error = "error"


class Systems (models.Model):
    name = models.CharField(max_length=100)

class AgenceSystems (models.Model):
    agenceID = models.ForeignKey(Agence)
    systemID = models.ForeignKey(Systems)


class Alerts (models.Model):
    type = models.IntegerField()
    text = models.CharField(max_length=255)
    chef_only = models.CharField(max_length=50,default='yes')
    systemID = models.ForeignKey(Systems)


class agenceStatus(enumerate):
    waiting = "waiting"
    in_progress = "in_progress"
    done = "done"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class AgenceAlerts (models.Model):
    agenceID = models.ForeignKey(Agence)
    alertID = models.ForeignKey(Alerts)
    alertDate = models.DateTimeField()
    fixedDate = models.DateTimeField()
    userID = models.ForeignKey(Users)
    status = models.IntegerField()


class Cities (models.Model):
    city = models.CharField(max_length=150)
