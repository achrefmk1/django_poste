# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-09-01 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostTN', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostTN.Systems'),
            preserve_default=False,
        ),
    ]
