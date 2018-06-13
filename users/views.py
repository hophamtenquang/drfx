# -*- coding: utf-8 -*-
from rest_framework import generics

from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated


class UserListView(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = models.CustomUser.objects.all()
        return queryset
