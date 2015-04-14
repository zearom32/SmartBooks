# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20150414_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
