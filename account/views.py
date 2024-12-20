from django.shortcuts import render, redirect

from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def login(request):
    return render(request, 'account/login.html')

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

def dashboard(request):
    pass

def profile(request):
    pass