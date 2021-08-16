# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-12 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostTN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgenceSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostTN.Agence')),
            ],
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='agencesystems',
            name='systemID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostTN.Systems'),
        ),
        migrations.AddField(
            model_name='alerts',
            name='systemID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='PostTN.Systems'),
            preserve_default=False,
        ),
    ]