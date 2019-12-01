# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=60)),
                ('hood_location', models.CharField(max_length=60)),
                ('occupants', models.IntegerField()),
            ],
        ),
    ]
