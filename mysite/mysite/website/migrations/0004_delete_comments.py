# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
