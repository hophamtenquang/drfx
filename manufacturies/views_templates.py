from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


def factory_view(request):
    if request.user.is_authenticated:
        return render(request, 'factory/list_factories.html')
    else:
        return render(request, 'home/login.html')
