# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile (models.Model):
    matricule = models.IntegerField()
    is_chef = models.CharField(max_length=50, default='yes')
    work_area = models.CharField(max_length=50)
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=256, blank=True, null=True)


class Agence (models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    userID = models.OneToOneField(User)


class Systems (models.Model):
    name = models.CharField(max_length=100)
    agences = models.ManyToManyField(Agence)


class Alerts (models.Model):
    type = models.IntegerField()
    text = models.CharField(max_length=255)
    chef_only = models.CharField(max_length=50, default='yes')
    systemID = models.ForeignKey(Systems)


class Cities (models.Model):
    city = models.CharField(max_length=150)


class Notification (models.Model):
    agence = models.ForeignKey(Agence)
    system = models.ForeignKey(Systems)
    alert = models.ForeignKey(Alerts)
    message = models.CharField(max_length=255)
    alertDate = models.DateTimeField()
    fixedDate = models.DateTimeField()
    user = models.ForeignKey(User)
    status = models.IntegerField()

