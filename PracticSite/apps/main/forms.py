from django import forms
from .models import UserInfo


class UserPhotoForm(forms.ModelForm):
	photo = forms.ImageField(label='Фотография')

	class Meta:
		model = UserInfo
		fields = ['photo']
