# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20160706_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateField(default=datetime.date.today, verbose_name='Deadline'),
        ),
    ]