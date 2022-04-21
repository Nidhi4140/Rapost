
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'designing/basic.html')

def home(request):
    return render(request, 'designing/home.html')

def signup(request):
    return render(request, 'designing/signup.html')

def login(request):
    return render(request, 'designing/login.html')

# def dashboard(request):
#     return render(request, 'designing/dashboard.html')
# @login_required
def dashboard(request):
    return render(request, 'designing/dashboard.html')

def hire(request):
    return render(request, 'designing/hire.html')

def feedback(request):
    return render(request, 'designing/feedback.html')

def aboutus(request):
    return render(request, 'designing/aboutus.html')
