# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20160502_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='Shipment_Note',
            field=models.TextField(max_length=500, null=True, verbose_name='\u0410\u0447\u0430\u0430\u043d\u044b \u0442\u044d\u043c\u0434\u044d\u0433\u043b\u044d\u043b'),
        ),
    ]