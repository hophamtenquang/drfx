# users/serializers.py
from rest_framework import serializers
from .models import Manufactory
from django.db.models import Q


class ManufactoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactory
        fields = ('id', 'title', 'code', 'created_user')