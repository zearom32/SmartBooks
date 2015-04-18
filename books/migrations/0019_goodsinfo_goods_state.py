# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20150418_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_state',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
