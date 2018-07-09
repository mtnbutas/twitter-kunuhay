# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tweet(models.Model):
	owner = models.ForeignKey(User, related_name='tweet')
	slug = models.CharField(max_length = 500)
	content = models.TextField(blank=False)
	create_date = models.DateTimeField(auto_now_add = True)
	likes = models.PositiveIntegerField(default=0)
	retweet = models.PositiveIntegerField(default=0)
	root = models.ForeignKey(Tweet, related_name='root_tweet')
	parent = models.ForeignKey(Tweet, related_name='parent_tweet')
	child = models.ForeignKey(Tweet, related_name='child_tweet')
