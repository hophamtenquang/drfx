# -*- coding: utf-8 -*-
from rest_framework import generics

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        import pdb
        pdb.set_trace()
        queryset = models.CustomUser.objects.all()
        return queryset
