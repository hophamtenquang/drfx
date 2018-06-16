# -*- coding: utf-8 -*-
from rest_framework import generics, viewsets

from models import Product
from django.db.models import Q
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from difflib import SequenceMatcher


class ProductListView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductListSerializer
    permission_classes = (IsAuthenticated,)
    paginate_by = 100  # 10 records per page
    paginate_by_param = 'page_size'  # ?page_size=1
    max_paginate_by = 1000  # limit 1000

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.GET.get('category', None)
        factory = self.request.GET.get('factory', None)
        searchText = self.request.GET.get('searchText', None)

        if category and category != '-1':
            queryset = queryset.filter(category=category)
        if factory and factory != '-1':
            queryset = queryset.filter(factory=factory)
        if searchText:
            queryset = queryset.filter(
                Q(title__icontains=searchText) | Q(code=searchText)
            )

        return queryset


    def create(self, request, *args, **kwargs):
        request.data['created_user'] = request.user.id

        title = request.data['title']
        check, similar_title = check_if_title_is_similar(title)
        import pdb
        pdb.set_trace()
        if check:
            raise exceptions.ValidationError({'similar_title' : 'Tên gần giống với {}. Không thể tạo'.format(similar_title.encode('utf-8').strip())});
        return super(ProductListView, self).create(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductDetailSerializer


    def get_queryset(self):
        return Product.objects.all()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def check_if_title_is_similar(title):
    all_products = Product.objects.all()
    title = title.strip()
    for p in all_products:
        if similar(title, p.title) > 0.8:
            return True, p.title
    return False, ''