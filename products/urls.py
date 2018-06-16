# users/urls.py
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    url('all', csrf_exempt(views.ProductListView.as_view()), name='product-list'),
    url(
        regex=r'^product/(?P<pk>\d+)/$',
        view=views.ProductDetailView.as_view(),
        name='product-detail'
    )
]
