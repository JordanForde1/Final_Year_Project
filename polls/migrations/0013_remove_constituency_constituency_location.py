# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-24 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_constituency_constituency_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constituency',
            name='constituency_location',
        ),
    ]
