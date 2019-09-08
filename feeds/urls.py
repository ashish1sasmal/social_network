
from django.urls import path,include
from . import views

urlpatterns = [

    path('post/',views.PostView.as_view(),name='feeds'),]
