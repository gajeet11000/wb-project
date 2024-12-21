from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm
from django.contrib import auth

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'account/index.html')

def login(request):
    login_form = LoginForm()
    
    if request.method == 'POST':
        filled_form = LoginForm(request, request.POST)
        if filled_form.is_valid():
            auth.login(request, filled_form.cleaned_data.get('user'))
            messages.success(request, "Logged in successfully.", extra_tags="login")
            return redirect('dashboard')
        else:
            return render(request, 'account/login.html', {'form': filled_form})
    
    return render(request, 'account/login.html', {'form': login_form})

def register(request):
    register_form = CreateUserForm()
    
    if request.method == 'POST':
        filled_form = CreateUserForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, "Registered successfully.", extra_tags="register")
            return redirect('login')
        else:
            return render(request, 'account/register.html', {'form': filled_form})
    
    return render(request, 'account/register.html', {'form': register_form})

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'account/profile.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully.", extra_tags="logout")
    return redirect('index')

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'account/change_password.html'
    login_url = 'login'
    
    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully.", extra_tags="password_change")
        return super().form_valid(form)