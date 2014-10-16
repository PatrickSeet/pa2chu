# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chu2pa', '0002_auto_20141015_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='hour',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
