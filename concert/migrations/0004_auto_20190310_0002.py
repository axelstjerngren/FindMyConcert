# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0003_auto_20190308_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='artist',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='description',
            field=models.CharField(max_length=560),
        ),
        migrations.AlterField(
            model_name='concert',
            name='end_time',
            field=models.TimeField(verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=models.ImageField(null=True, upload_to='concert_images'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='start_time',
            field=models.TimeField(verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concert', to='concert.Venue'),
        ),
    ]
