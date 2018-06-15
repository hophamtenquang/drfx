# api/urls.py
from django.conf.urls import url, include

urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^factories/', include('manufacturies.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
