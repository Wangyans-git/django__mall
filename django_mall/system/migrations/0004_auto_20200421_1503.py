# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-21 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20200417_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagefile',
            options={'verbose_name': '图片表', 'verbose_name_plural': '图片表'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-reorder'], 'verbose_name': '新闻管理', 'verbose_name_plural': '新闻管理'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-reorder'], 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
    ]
