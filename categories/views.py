# -*- coding: utf-8 -*-
from rest_framework import generics

from models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = serializers.CategoryListSerializer
    permission_classes = (IsAuthenticated,)
    paginate_by = 10  # 10 records per page
    paginate_by_param = 'page_size'  # ?page_size=1
    max_paginate_by = 1000  # limit 1000

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
