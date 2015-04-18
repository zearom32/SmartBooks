# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20150418_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='sell_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 16, 20, 1, 529582), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 16, 20, 8, 254821), auto_now=True),
            preserve_default=False,
        ),
    ]
