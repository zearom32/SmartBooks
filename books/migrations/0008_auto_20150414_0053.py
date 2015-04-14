# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20150414_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]
