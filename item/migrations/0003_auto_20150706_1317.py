# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20150706_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good_additional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('image', models.ImageField(upload_to=b'image', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('price', models.IntegerField(default=0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
            ],
        ),
        migrations.RemoveField(
            model_name='options',
            name='publications',
        ),
        migrations.AddField(
            model_name='good',
            name='continuous_operation',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb5\xd0\xbf\xd1\x80\xd0\xb5\xd1\x80\xd1\x8b\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='cooling_system',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa1\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xbe\xd1\x85\xd0\xbb\xd0\xb0\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='dimensions',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd1\x8b (\xd0\x94\xd1\x85\xd0\xa8\xd1\x85\xd0\x92)', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='displacement',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xbc \xd0\xb4\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='fuel',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x82\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='fuel_capacity',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xbc \xd1\x82\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb1\xd0\xb0\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='fuel_consumption',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4 \xd1\x82\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='noise_level',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x88\xd1\x83\xd0\xbc\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='number_of_cylinders',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe \xd1\x86\xd0\xb8\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb4\xd1\x80\xd0\xbe\xd0\xb2', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='number_of_phases',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd1\x84\xd0\xb0\xd0\xb7', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='performance',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x98\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='power',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9c\xd0\xbe\xd1\x89\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='power_dvig',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb4\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='rotational_speed',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81\xd1\x82\xd0\xbe\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='startup_type',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='voltage',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd1\x8f\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='good',
            name='weight',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xb5\xd1\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to=b'image', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.AddField(
            model_name='good',
            name='good_additional',
            field=models.ManyToManyField(to='item.Good_additional', verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f'),
        ),
    ]
