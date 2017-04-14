# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170331_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
