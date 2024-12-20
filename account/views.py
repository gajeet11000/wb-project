from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def login(request):
    pass

def register(request):
    pass

def dashboard(request):
    pass

def profile(request):
    pass