# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreosteoweb', '0035_auto_20190427_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='type',
            field=models.CharField(blank=True, default='invoice', max_length=10, verbose_name='Invoice type'),
        ),
    ]
