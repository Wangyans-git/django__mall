# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-13 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='登陆的账号')),
                ('ip', models.CharField(max_length=32, verbose_name='登陆的ip')),
                ('address', models.CharField(blank=True, max_length=32, null=True, verbose_name='登陆的地址')),
                ('source', models.CharField(max_length=32, verbose_name='登陆的来源')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='登陆的时间')),
            ],
            options={
                'db_table': 'accounts_login_record',
            },
        ),
        migrations.CreateModel(
            name='PasswordChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('avatar', models.ImageField(null=True, upload_to='avatar', verbose_name='头像')),
                ('integral', models.IntegerField(default=0, verbose_name='用户积分')),
                ('level', models.SmallIntegerField(default=0, verbose_name='用户等级')),
            ],
            options={
                'db_table': 'acounts_user',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=32, verbose_name='省份')),
                ('city', models.CharField(max_length=32, verbose_name='城市')),
                ('area', models.CharField(max_length=32, verbose_name='区域')),
                ('town', models.CharField(blank=True, max_length=32, null=True, verbose_name='街道')),
                ('address', models.CharField(max_length=64, verbose_name='详细地址')),
                ('username', models.CharField(max_length=32, verbose_name='收件人')),
                ('phone', models.CharField(max_length=20, verbose_name='收件人电话,')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否为默认地址')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
            options={
                'db_table': 'account_user_address',
                'ordering': ['is_default', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=32, verbose_name='真实姓名')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='邮箱')),
                ('is_email', models.BooleanField(default=False, verbose_name='邮箱是否已经验证注册')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码')),
                ('is_phone', models.BooleanField(default=False, verbose_name='手机号是否验证')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='性别')),
                ('age', models.SmallIntegerField(default=0, verbose_name='年龄')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
            options={
                'db_table': 'account_user_profile',
            },
        ),
        migrations.AddField(
            model_name='loginrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
