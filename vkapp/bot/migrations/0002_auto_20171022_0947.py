# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-22 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminreview',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.News', unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.News', unique=True),
        ),
    ]