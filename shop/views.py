from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def usermaster(request):
    return render(request, 'usermaster.html')

def myprofile(request):
    return render(request, 'myprofile.html')

def springwhites(request):
    return render(request, 'springwhites.html')

