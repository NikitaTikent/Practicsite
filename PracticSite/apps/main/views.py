from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
	return render(request, 'base.html')


def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main:index')
		else:
			return redirect('main:index')
	else:
		return render(request, 'log_in.html')


def log_out(request):
	logout(request)
	return redirect('main:index')


def personal(request):
	if request.user.is_authenticated():
		pass
	else:
		redirect('main:log_in')
