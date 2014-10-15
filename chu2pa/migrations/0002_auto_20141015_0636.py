# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chu2pa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='status',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
