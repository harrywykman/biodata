# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biota', '0006_auto_20160411_2117'),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientific_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biota.ScientificName')),
            ],
        ),
    ]
