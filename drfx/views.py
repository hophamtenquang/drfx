from django.shortcuts import render
from django.contrib.auth import logout


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/login.html')


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/login.html')
