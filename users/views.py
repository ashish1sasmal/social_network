from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate
# Create your views here.

class Home(TemplateView):
	template_name='users/home.html'

def login_signup(request):
	
	if request.method=='POST' and 'login' in request.POST:
		username=request.POST.get('username')
		password=request.POST.get('password')
		print(username)
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect('home')
		else:
			return redirect('login_signup')




	elif request.method=='POST' and 'signup' in request.POST:
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		dob=request.POST.get('DOB')
		gender=request.POST.get('gender')
		user=User(username=email,first_name=first_name,last_name=last_name,email=email,password=password)
		profile=Profile(dob=dob,gender=gender)

		user.save()
		profile.save()

		return redirect('home')

	return render(request,'users/login_signup.html')


					
