# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-03 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='file_size',
            field=models.CharField(default='0M', max_length=30),
        ),
    ]
