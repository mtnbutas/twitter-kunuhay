# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def avatar_upload_path(instance, filename):
	return './avatars/user_{}_{}'.format(instance.user.username, filename)
	
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=161, blank=True)
    avatar = models.FileField(upload_to=avatar_upload_path, blank=True)

	@property
	def avatar_url(self):
		if self.avatar:
			return self.avatar.url
		return static('img/default_avatar.png')

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name



