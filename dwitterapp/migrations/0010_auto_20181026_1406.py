# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitterapp', '0009_auto_20181026_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
