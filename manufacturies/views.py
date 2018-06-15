# -*- coding: utf-8 -*-
from rest_framework import generics

from models import Manufactory
from . import serializers
from rest_framework.permissions import IsAuthenticated


class ManufactoryListView(generics.ListCreateAPIView):
    serializer_class = serializers.ManufactoryListSerializer
    permission_classes = (IsAuthenticated,)
    paginate_by = 100  # 10 records per page
    paginate_by_param = 'page_size'  # ?page_size=1
    max_paginate_by = 1000  # limit 1000

    def get_queryset(self):
        queryset = Manufactory.objects.all()
        return queryset


    def create(self, request, *args, **kwargs):
        request.data['created_user'] = request.user.id
        return super(ManufactoryListView, self).create(request, *args, **kwargs)
