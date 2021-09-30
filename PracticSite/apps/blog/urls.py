from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('article/<int:article_pk>', views.article, name='article'),
	path('add_article/', views.add_article, name='add_article'),
	path('update_article/<int:article_pk>/', views.update_article, name='update_article'),
	path('delete_article/<int:article_pk>/', views.delete_article, name='delete_article')
]
