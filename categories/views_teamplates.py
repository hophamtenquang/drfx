from django.shortcuts import render


def category_list_view(request):
    if request.user.is_authenticated:
        return render(request, 'category/list_categories.html')
    else:
        return render(request, 'home/login.html')
