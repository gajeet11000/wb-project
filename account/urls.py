from django.urls import path, include

from . import views

urlpatterns = [
    path('account/register', views.register, name='register'),
    path('account/login', views.login, name='login'),
    path('account/logout', views.logout, name='logout'),
    
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
]