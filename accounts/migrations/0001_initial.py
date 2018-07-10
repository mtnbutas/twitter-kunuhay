# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bio', models.TextField(max_length=161, blank=True)),
                ('avatar', models.FileField(upload_to=accounts.models.avatar_upload_path, blank=True)),
                ('header', models.FileField(upload_to=accounts.models.header_upload_path, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
