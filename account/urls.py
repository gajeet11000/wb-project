from django.urls import path, include

from . import views

urlpatterns = [
    path('account/login', views.login, name='login'),
    path('account/register', views.register, name='register'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
]