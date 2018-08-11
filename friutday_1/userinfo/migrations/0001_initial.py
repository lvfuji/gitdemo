# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(db_column='aname', verbose_name='姓名', max_length=30)),
                ('address', models.CharField(db_column='address', verbose_name='收站点', max_length=150)),
                ('cellphone', models.CharField(db_column='cellphone', verbose_name='手机号', max_length=15)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_column='uemail', verbose_name='邮箱', max_length=40)),
                ('uname', models.CharField(db_column='uname', verbose_name='用户名', max_length=50)),
                ('upassword', models.CharField(db_column='upassword', verbose_name='密码', max_length=200)),
                ('isban', models.BooleanField(default=False, verbose_name='禁用')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to='userinfo.UserInfo'),
        ),
    ]
