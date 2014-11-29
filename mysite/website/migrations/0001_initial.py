# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data', models.DateTimeField(verbose_name='published_time')),
                ('title', models.CharField(max_length=20000)),
                ('url', models.CharField(max_length=20000)),
                ('words', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
