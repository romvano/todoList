# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 14:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20160706_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 14, 30, 7, 514895, tzinfo=utc), verbose_name='Deadline'),
        ),
    ]