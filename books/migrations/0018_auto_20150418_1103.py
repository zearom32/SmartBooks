# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20150418_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='numbers',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='source',
            field=models.URLField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
