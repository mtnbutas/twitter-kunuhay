# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def login(request):
	return render(request, 'login.html', {})

def userfeed(request):
	return render(request, 'userfeed.html', {})

def registration(request):
	return render(request, 'registration.html', {})

def signup(request):
	return render(request, 'signup.html', {})