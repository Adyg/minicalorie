# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicalorie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasrc',
            name='authors',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='end_page',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='issue_state',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='journal',
            field=models.CharField(blank=True, max_length=135, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='start_page',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='vol_city',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='datasrc',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='cho_factor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='comname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='fat_factor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='manufacname',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='n_factor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='pro_factor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='ref_desc',
            field=models.CharField(blank=True, max_length=135, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='refuse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='sciname',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='fooddes',
            name='survey',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='footnote',
            name='nutr_no',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='add_nutr_mark',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='addmod_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='cc',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='deriv_cd',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='df',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='low_eb',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='max',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='min',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='num_studies',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='ref_ndb_no',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='stat_cmt',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutdata',
            name='up_eb',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrdef',
            name='tagname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weight',
            name='num_data_pts',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]