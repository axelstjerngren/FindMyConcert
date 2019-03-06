# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-05 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0002_auto_20190305_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giggoer',
            old_name='interests',
            new_name='comments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='giggoer',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarks', to='concert.Concert'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='concerts',
            field=models.ManyToManyField(related_name='concerts', to='concert.Concert'),
        ),
    ]
