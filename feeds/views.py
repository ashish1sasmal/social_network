from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView
# from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class Feeds(TemplateView):
	template_name='feeds/feeds.html'


class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['text','image']

	def form_valid(self,form):  #NOT NULL constraint failed: blog_post.author_id
		form.instance.author=self.request.user    #saving user before creating post i.e., we are overriding it
		return super().form_valid(form)

class FeedsView(ListView):
	template_name='feeds/feeds.html'
	context_object_name='posts'
	model=Post
	ordering=['-date_posted']




