# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biota', '0005_auto_20160410_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxon',
            name='authority',
        ),
        migrations.DeleteModel(
            name='Authority',
        ),
    ]
