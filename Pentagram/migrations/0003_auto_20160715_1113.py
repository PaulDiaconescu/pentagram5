# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 08:13
from __future__ import unicode_literals

import Pentagram.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to=Pentagram.models.photos_directory),
        ),
    ]
