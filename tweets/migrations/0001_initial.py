# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('favorites', models.PositiveIntegerField(default=0)),
                ('retweet', models.PositiveIntegerField(default=0)),
                ('child', models.ForeignKey(related_name='child_tweet', to='tweets.Tweet')),
                ('owner', models.ForeignKey(related_name='tweet', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(related_name='parent_tweet', to='tweets.Tweet')),
                ('root', models.ForeignKey(related_name='root_tweet', to='tweets.Tweet')),
            ],
        ),
    ]
