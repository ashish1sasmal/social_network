
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    
    path('login_signup/',views.login_signup,name="login_signup"),
    path('',views.Home.as_view(),name='home'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/login_signup.html'),name='logout'),
]
