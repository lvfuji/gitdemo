# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='名称', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品价格')),
                ('desc', models.CharField(verbose_name='描述', max_length=1000)),
                ('picture', models.ImageField(default='normal.png', verbose_name='商品照片', upload_to='static/images/goods')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='名称', max_length=30)),
                ('desc', models.CharField(default='商品描述', verbose_name='描述', max_length=200)),
                ('flag', models.IntegerField(default=0)),
                ('picture', models.ImageField(default='normal.png', upload_to='static/image/good_type')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'goods_Type',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(to='memberapp.GoodsType'),
        ),
    ]
