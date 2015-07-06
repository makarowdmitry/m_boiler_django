# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name=b'\xd0\xa5\xd0\xb0\xd1\x80\xd0\xb0\xd0\xba\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd0\xb8\xd0\xba\xd0\xb0')),
                ('value', models.CharField(max_length=1000, verbose_name=b'\xd0\x97\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=1000, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AddField(
            model_name='options',
            name='publications',
            field=models.ManyToManyField(to='item.Good'),
        ),
    ]
