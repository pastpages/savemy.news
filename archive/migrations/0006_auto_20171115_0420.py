# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20171115_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='memento',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
