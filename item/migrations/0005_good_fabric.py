# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20150706_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='fabric',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True),
        ),
    ]
