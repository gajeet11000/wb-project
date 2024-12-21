from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account/register', views.register, name='register'),
    path('account/login', views.login, name='login'),
    path('account/logout', views.logout, name='logout'),
    
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    path(
        "reset_password/", 
         auth_views.PasswordResetView.as_view(template_name="account/password_reset/password_reset.html"),
         name="reset_password"
    ),
    
    path(
        "reset_password_sent/", 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset/password_reset_sent.html"), 
        name="password_reset_done"
    ),
    
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset/password_reset_form.html"),
         name="password_reset_confirm"
    ),
    
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset/password_reset_complete.html"),
        name="password_reset_complete"
    ),
]