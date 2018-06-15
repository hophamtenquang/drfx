# users/serializers.py
from rest_framework import serializers
from .models import Category
from django.db.models import Q


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'code', 'created_user')

    def validate(self, data):

        ERROR_MESSAGE = "Cannot creat. Duplicate code or title."

        code = data.get('code', None)
        title = data.get('title', None)
        try:
            if code:
                c1 = Category.objects.get(
                    Q(code=code) |
                    Q(title=title)
                )
                if c1:
                    raise serializers.ValidationError({'Exists': ERROR_MESSAGE})

        except Category.DoesNotExist:
            return data
        except Category.MultipleObjectsReturned:
            raise serializers.ValidationError({'Exists': ERROR_MESSAGE})