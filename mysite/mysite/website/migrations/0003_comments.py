# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_url_is_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
