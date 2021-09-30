from django.shortcuts import render, redirect
from django.http import Http404

from . import services
from .models import Article, ArticleComments, User


def index(request):
	articles = Article.objects.all()
	context = {'articles': articles}
	return render(request, 'blog/index.html', context)


def article(request, article_pk):
	if request.method == 'POST':
	 	services.add_article_comment(request, article_pk)
	
	article = Article.objects.get(pk=article_pk)
	comments = ArticleComments.objects.filter(article=article)
	context = {'article': article, 'comments': comments}
	return render(request, 'blog/article.html', context)


def update_article(request, article_pk):
	return services.update_article(request, article_pk)


def delete_article(request, article_pk):
	return services.delete_article(request, article_pk)


def add_article(request):
	return services.add_article(request)
