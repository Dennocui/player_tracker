from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm


def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#redirect to Home
			return HttpResponseRedirect(reverse('players:home'))
		else:
			messages.error(request, 'Bad Username or Password')

	return render(request, 'accounts/login.html', {})


def logout_user(request):
	#return render(request, 'accounts/logout.html', {})
	logout(request)
	return HttpResponseRedirect(reverse('accounts:login'))

def user_registration(request):
	
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password =  form.cleaned_data['password1']
			email = form.cleaned_data['email']
			user = User.objects.create_user(username, email=email, password=password)
			messages.success(request, 'User {} Registered Successfuly'.format(user.username))
			return HttpResponseRedirect(reverse('players:settings'))

	else:
		#context = {'form':form}
		
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'form': form})