# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    code = models.CharField(
        blank=True, help_text=('Only For Developers'), max_length=20, null=True
    )
    title = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(
        CustomUser, blank=True, null=True, related_name='product_created_user',
    )
