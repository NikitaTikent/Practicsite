from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	title = models.CharField(max_length=100, verbose_name='Название')
	article = models.TextField(verbose_name='Статья')
	date = models.DateField(auto_now=True)

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		ordering = ['-date']


class ArticleComments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
	comment = models.CharField(max_length=200, verbose_name='Комментарий')

	def __str__(self):
		return str(self.comment)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['-id']
