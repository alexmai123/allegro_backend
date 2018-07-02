# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-27 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(null=True, to='main.Role'),
        ),
    ]