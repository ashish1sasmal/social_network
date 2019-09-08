
from django.urls import path,include

from . import views
urlpatterns = [
    path('profile/edit/',views.edit_profile,name='edit-profile'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]
