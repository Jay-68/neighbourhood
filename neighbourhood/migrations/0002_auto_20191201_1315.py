# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-01 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]