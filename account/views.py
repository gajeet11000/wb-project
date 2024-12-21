from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm
from django.contrib import auth

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def login(request):
    login_form = LoginForm()
    
    if request.method == 'POST':
        filled_form = LoginForm(request, request.POST)
        if filled_form.is_valid():
            auth.login(request, filled_form.cleaned_data.get('user'))
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
    return redirect('index')