from django import forms

from .models import Article, User


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'article']
