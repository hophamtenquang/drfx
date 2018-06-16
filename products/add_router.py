# users/urls.py
from django.conf.urls import url

from . import views_templates

urlpatterns = [
    url(r'', views_templates.product_add_view, name='add_products'),
]
