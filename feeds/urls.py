
from django.urls import path,include
from . import views

urlpatterns = [

    path('post/',views.Feeds.as_view(),name='feeds'),
    path('post/create/',views.PostCreateView.as_view(),name='create')
]