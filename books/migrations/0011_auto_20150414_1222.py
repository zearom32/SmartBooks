# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_bookinfo_doubanid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='publidate',
            new_name='pubdate',
        ),
    ]
