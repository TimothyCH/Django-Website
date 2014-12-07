# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 12, 20, 12, 890000, tzinfo=utc), verbose_name=b'comment_time'),
            preserve_default=False,
        ),
    ]
