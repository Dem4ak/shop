# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170331_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]