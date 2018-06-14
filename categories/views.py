# -*- coding: utf-8 -*-
from rest_framework import generics

from models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = serializers.CategoryListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
