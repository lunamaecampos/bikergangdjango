# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-05 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeradmin', '0002_artistprofile_currentartist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistprofile',
            name='artistmgmtemail',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
