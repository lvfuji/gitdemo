# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ccount', models.IntegerField(db_column='cart_count', verbose_name='数量')),
                ('good', models.ForeignKey(db_column='good_id', to='memberapp.Goods')),
                ('user', models.ForeignKey(db_column='user_id', to='userinfo.UserInfo')),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(verbose_name='订单号', max_length=200)),
                ('ads', models.CharField(verbose_name='收件人', max_length=200)),
                ('acot', models.CharField(verbose_name='总数', max_length=200)),
                ('acounts', models.CharField(verbose_name='价格', max_length=200)),
                ('cals', models.TextField(null=True, blank=True, verbose_name='orderdetail')),
                ('orderStatus', models.IntegerField(default='1', blank=True, verbose_name='订单状态', choices=[(1, '未支付'), (2, '已支付'), (3, '订单取消')])),
                ('user', models.ForeignKey(db_column='user_id', to='userinfo.UserInfo')),
            ],
        ),
    ]
