# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171015_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='descricao',
            field=models.CharField(max_length=100, null=True),
        ),
    ]