# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20150414_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='book',
            field=models.ForeignKey(related_name=b'goods', to='books.BookInfo'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='seller',
            field=models.ForeignKey(related_name=b'goods', to=settings.AUTH_USER_MODEL),
        ),
    ]
