# users/serializers.py
from rest_framework import serializers
from . import models


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('title', 'code', 'created_user')
