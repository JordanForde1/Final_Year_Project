# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='question',
        ),
        migrations.DeleteModel(
            name='Tax',
        ),
    ]
