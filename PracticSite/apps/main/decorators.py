from django.shortcuts import redirect


def is_auth(func):
	def wrapp(request, *args, **kwargs):
		if request.user.is_authenticated:
			return func(request, *args, **kwargs)
		else:
			return redirect('main:log_in')
	return wrapp
