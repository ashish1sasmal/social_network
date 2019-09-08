from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def edit_profile(request):
	user=request.user
	profile=request.user.profile
	if request.method=='POST':
		first_name=request.POST.get('fname')
		last_name=request.POST.get('lname')
		website=request.POST.get('website')
		bio=request.POST.get('bio')
		email=request.POST.get('email')
		phone=request.POST.get('phone')


#########################################

		user.first_name=first_name
		user.last_name=last_name
		user.email=email
		user.username=email
		user.save()

########################################

		profile.website=website
		profile.bio=bio
		profile.phone=phone
		if 'profile_pic' in request.FILES:
			profile.image=request.FILES['profile_pic']
		profile.save()

#########################################3

		return redirect('profile')


	return render(request,'userprofile/edit_profile.html',{'user':user,'profile':profile})
