# users/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.CategoryListView.as_view()),
]
