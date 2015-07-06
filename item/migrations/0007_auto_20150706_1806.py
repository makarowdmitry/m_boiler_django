# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20150706_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='power',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9c\xd0\xbe\xd1\x89\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
        ),
    ]
