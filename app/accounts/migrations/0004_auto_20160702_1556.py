# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-02 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160119_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 15, 56, 9, 28712)),
        ),
    ]
