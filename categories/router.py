# users/urls.py
from django.conf.urls import url

from . import views_teamplates

urlpatterns = [
    url('', views_teamplates.category_list_view, name='list_categories'),
]
