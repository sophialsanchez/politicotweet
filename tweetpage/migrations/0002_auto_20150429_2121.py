# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='imc_src',
            new_name='img_src',
        ),
    ]
