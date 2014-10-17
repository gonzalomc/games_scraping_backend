# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='console',
            field=models.ForeignKey(default=1, to='games.Console'),
            preserve_default=False,
        ),
    ]
