# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicalorie', '0002_auto_20170509_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddes',
            name='refuse',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]
