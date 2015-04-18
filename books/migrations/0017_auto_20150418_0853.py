# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20150418_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='description',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='quality',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
    ]
