# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20150418_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='sell_time',
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='update_time',
        ),
    ]
