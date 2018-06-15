# users/urls.py
from django.conf.urls import url

from . import views_templates

urlpatterns = [
    url('', views_templates.factory_view, name='list_factories'),
]
