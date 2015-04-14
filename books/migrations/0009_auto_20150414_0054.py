# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20150414_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
    ]
