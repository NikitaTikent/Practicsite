from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import ArticleForm
from .models import Article, ArticleComments

def add_article(request):
	if request.user.has_perm('blog.add_article'):
		if request.method == 'POST':
			form = ArticleForm(request.POST)
			if form.is_valid():
				article = Article()
				user = User.objects.get(username=request.user.username)
				article.user = user
				article.title = form.cleaned_data['title']
				article.article = form.cleaned_data['article']
				article.save()
				return redirect('blog:index')
			else:
				context = {'form': form}
				return render(request, 'blog/add_article.html', context)
		else:
			form = ArticleForm()
			context = {'form': form}
			return render(request, 'blog/add_article.html', context)
	else:
		raise Http404('Ошибка доступа')


def update_article(request, article_pk: int):
	if request.user.has_perm('blog.change_article'):
		if request.method == 'POST':
			form = ArticleForm(request.POST)
			if form.is_valid():
				article = Article.objects.get(pk=article_pk)
				user = User.objects.get(username=request.user.username)
				article.user = user
				article.title = form.cleaned_data['title']
				article.article = form.cleaned_data['article']
				article.save()
				return redirect('blog:index')
			else:
				context = {'form': form}
				return render(request, 'blog/add_article.html', context)
		else:
			article = Article.objects.get(pk=article_pk)
			form = ArticleForm(instance=article)
			context = {'form': form}
			return render(request, 'blog/add_article.html', context)
	else:
		raise Http404('Ошибка доступа')


def delete_article(request, article_pk: int):
	article = Article.objects.get(pk=article_pk)
	if request.method == 'POST':
		perms = request.user.has_perm('blog.delete_article')
		autor = article.user
		request_user = User.objects.get(username=request.user.username)
		if perms and autor == request_user:
			article.delete()
			return redirect('blog:index')
		else:
			raise Http404('Ошибка доступа')
	else:
		return render(request, 'blog/delete_article.html', {'article': article})


def add_article_comment(request, article_pk: int):
	username = request.user.username
	user = User.objects.get(username=request.user.username)
	article = Article.objects.get(pk=article_pk)
	comment = request.POST['comment']
	ArticleComments.objects.create(user=user, article=article, comment=comment)
