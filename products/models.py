# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import CustomUser
from categories.models import Category
from manufacturies.models import Manufactory


# Create your models here.
class Product(models.Model):
    code = models.CharField(
        blank=True, help_text=('Only For Developers'), max_length=20, null=True, unique=True
    )
    title = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(
        CustomUser, blank=True, null=True,
    )
    category = models.ForeignKey(
        Category, blank=True, null=True, related_name='product_category',
    )
    factory = models.ForeignKey(
        Manufactory, blank=True, null=True, related_name='product_factory',
    )
    key = models.CharField(
        blank=True, help_text=('Only For Developers'), max_length=20, null=True
    )
    description = models.TextField(null=True, blank=True)


    class Meta:
        unique_together = ('title', 'key', 'factory')


# class Sequence(object):
#     @staticmethod
#     def get_sequence_number_deli(factory_id):
#         self.db.execute("SELECT count(*) FROM product WHERE factory=%s;", args=factory_id)
#         sequence = self.db.fetchone()
#         sequence_number = 0
#         if sequence:
#             sequence_number = sequence[0]
#         return "{word}_{number:04d}".format(word='D', number=sequence_number+1), sequence_number+1