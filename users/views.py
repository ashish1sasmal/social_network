from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
	template_name='users/home.html'

def signup(request):
	if request.method=='POST' and 'signup' in request.POST:
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