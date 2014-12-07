# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vtag', models.BooleanField(default=False)),
                ('btag', models.BooleanField(default=False)),
                ('ptag', models.BooleanField(default=False)),
                ('date', models.DateTimeField(verbose_name=b'published_time')),
                ('title', models.CharField(max_length=20000)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=2000)),
                ('data', models.ForeignKey(to='website.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
