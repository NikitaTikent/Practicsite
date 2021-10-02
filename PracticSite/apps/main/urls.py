from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
	path('log_in/', views.log_in, name='log_in'),
	path('log_out/', views.log_out, name='log_out'),
	path('personal_cab/', views.personal_cab, name='personal_cab'),
	path('user_articles/', views.user_articles, name='user_articles'),
	path('add_user_photo/', views.add_user_photo, name='add_user_photo'),
	path('delete_user_photo/', views.delete_user_photo, name='delete_user_photo')
]
