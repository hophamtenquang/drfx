from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


def product_add_view(request):
    if request.user.is_authenticated:
        return render(request, 'product/product_add.html')
    else:
        return render(request, 'home/login.html')

