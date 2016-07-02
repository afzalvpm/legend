# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='loading_capacity',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]