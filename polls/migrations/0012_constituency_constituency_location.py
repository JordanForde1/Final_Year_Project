# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-24 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_constituency_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituency',
            name='constituency_location',
            field=models.IntegerField(default=0),
        ),
    ]
