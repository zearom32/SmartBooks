# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_bookinfo_has_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='author',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='pic_url',
            field=models.URLField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='publidate',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='publisher',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
