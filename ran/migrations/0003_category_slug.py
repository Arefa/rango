# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 03:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ran', '0002_auto_20151214_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 12, 14, 3, 15, 37, 463000, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
