# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 13:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20160706_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateField(default=datetime.date(2016, 7, 7), verbose_name='Deadline'),
        ),
    ]
