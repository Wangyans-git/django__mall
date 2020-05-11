# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-17 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=32, verbose_name='昵称'),
            preserve_default=False,
        ),
    ]
