# users/urls.py
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    url('', csrf_exempt(views.ManufactoryListView.as_view())),
]
