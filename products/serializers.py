# users/serializers.py
from rest_framework import serializers
from .models import Product
from django.db.models import Q


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'code', 'created_user', 'category', 'factory', 'key', 'description')
        read_only_fields = ['id']

    def validate(self, data):
        return data

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'code', 'created_user', 'category', 'factory', 'key', 'description')
        read_only_fields = ['id']

    def validate(self, data):
        return data