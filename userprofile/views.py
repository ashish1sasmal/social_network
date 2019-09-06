from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
# Create your views here.

def edit_profile(request):
	user=request.user
	profile=request.user.profile
	return render(request,'userprofile/edit_profile.html',{'user':user,'profile':profile})
