# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_auto_20151217_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgunit',
            name='ad_dn',
            field=models.CharField(editable=False, max_length=512, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='orgunit',
            name='ad_guid',
            field=models.CharField(editable=False, max_length=48, null=True, unique=True),
        ),
    ]
