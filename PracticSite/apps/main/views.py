from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import UserPhotoForm
from .models import UserInfo
from blog.models import Article


def index(request):
	return render(request, 'base.html')


def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main:personal_cab')
		else:
			messages.info(request, 'Проверьте правильность введённых данных')
			return redirect('main:log_in')
	else:
		return render(request, 'log_in.html')


def log_out(request):
	logout(request)
	return redirect('main:index')


def personal_cab(request):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		context = {}

		try:
			user_info = UserInfo.objects.get(user=user)
			context['user_info'] = user_info
		except:
			pass

		articles = Article.objects.filter(user=user)
		context['articles'] = articles

		return render(request, 'user/personal_cab.html', context)
	else:
		return redirect('main:log_in')


def user_articles(request):
	if request.user.is_authenticated:
		username = request.user.username
		user = User.objects.get(username=username)
		articles = Article.objects.filter(user=user)
		context = {'articles': articles}
		return render(request, 'user/user_articles.html', context)
	else:
		raise Http404('Ошибка доступа')

def add_user_photo(request):
	username = request.user.username
	user = User.objects.get(username=username)
	if request.method == 'POST':
		if request.user.is_authenticated:
			form = UserPhotoForm(request.POST, request.FILES)
			if form.is_valid():
				user_info = UserInfo()
				user_info.user = user
				user_info.photo = form.cleaned_data["photo"]
				user_info.save()
				return redirect('main:personal_cab')
			else:
				return render(request, 'user/add_photo.html', {'form': form})
		else:
			raise Http404('Ошибка доступа')
	else:
		form = UserPhotoForm(instance=user)
		context = {'form': form}
		return render(request, 'user/add_photo.html', context)


def delete_user_photo(request):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)

		try:
			user_photo = UserInfo.objects.get(user=user)
			user_photo.delete()
		except:
			raise Http404('Фотография отсутствует')

		return redirect('main:personal_cab')
	else:
		raise Http404('Вы не авторизованы')
