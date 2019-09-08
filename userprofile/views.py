from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
# Create your views here.



class ProfileView(LoginRequiredMixin,TemplateView):
	template_name='userprofile/profile.html'
	context_object_name = 'user'
	def get_queryset(self):
		return User.objects.filter(user=self.request.user)


@login_required

def edit_profile(request):
	user=request.user
	profile=request.user.profile
	return render(request,'userprofile/edit_profile.html',{'user':user,'profile':profile})
