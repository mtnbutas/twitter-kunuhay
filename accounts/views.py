# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json


import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):

	if request.method == 'POST':
		eou = request.POST['eou']
		password = request.POST['password']

	return render(request, 'login.html', {})

def userfeed(request):
	return render(request, 'userfeed.html', {})

def registration(request):
	return render(request, 'registration.html', {})

def signup(request):

	if request.method == 'POST':
		print request.body
		# data = json.loads(request.body.decode('utf-8'))

		username = request.get('name')
		email = request.get('email')
		password = request.get('password')

		new_user = User(username=username, email=email)
		new_user.set_password(password)
		new_user.save()

		new_account = models.Account(user=new_user)
		new_account.save()

		return redirect('login')

	return render(request, 'signup.html', {})

def login_view(request): 
	if request.user.is_authenticated():
		return redirect('userfeed')

	context = {}

	if request.method == "POST":
		data = json.loads(request.body.decode('utf-8'))

		eou = data.get('eou')
		password = data.get('password')
		user = authenticate(email=eou, password=password)

		if user is not None:
			auth_login(request, user)
			return redirect('userfeed')
		else:
			user =  authenticate(username=eou, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('userfeed')
			else:
				context['error'] = 'error'
				return JsonResponse({'status': 404})

	
	return render(request, 'login.html', context)