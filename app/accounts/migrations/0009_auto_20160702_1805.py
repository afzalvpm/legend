# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-02 18:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160702_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 18, 5, 12, 326779)),
        ),
    ]
