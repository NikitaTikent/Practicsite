from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		verbose_name='Пользователь')

	photo = models.ImageField(verbose_name='Фотография',
		upload_to='photo_user/')

	def __str__(self):
		return self.user.username

	def delete(self, *args, **kwargs):
		self.photo.delete(save=False)
		return super().delete(*args, **kwargs)

	class Meta:
		verbose_name = 'Пользовательская фотография'
		verbose_name_plural = 'Пользовательские фотографии'
