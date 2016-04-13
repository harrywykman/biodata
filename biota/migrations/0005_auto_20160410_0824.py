# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biota', '0004_auto_20160409_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScientificName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='taxon',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtaxa', to='biota.Taxon', verbose_name='supertaxon'),
        ),
        migrations.AddField(
            model_name='scientificname',
            name='genus_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subgenus', to='biota.Taxon'),
        ),
        migrations.AddField(
            model_name='scientificname',
            name='specific_epithet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subspecific', to='biota.Taxon'),
        ),
        migrations.AddField(
            model_name='scientificname',
            name='subspecific_epithet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subsubspecific', to='biota.Taxon'),
        ),
        migrations.AddField(
            model_name='taxon',
            name='authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biota.Authority'),
        ),
    ]