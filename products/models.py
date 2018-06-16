# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import CustomUser
from categories.models import Category
from manufacturies.models import Manufactory


# Create your models here.
class Product(models.Model):
    code = models.CharField(
        blank=True, help_text=('Only For Developers'), max_length=20, null=True
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
        unique_together = ('title', 'key', 'category')

    # def save(self, *args, **kwargs):
    #     if getattr(self, 'code', True):
    #         self.code = '{code}_{number:04d}'.format(code=self.category.code, number=self.id)
    #     super(Product, self).save(*args, **kwargs)

    # @staticmethod
    # def get_sequence_number(category_id, *args, **kwargs):
    #     project_id = kwargs.get('project_id', None)
    #     created = False
    #     if category_id:
    #         sequence = Sequence.objects.filter(company_id=company_id, project_id=project_id,
    #                                            content_id=content_type_id).first()
    #         if not sequence:
    #             sequence = Sequence.objects.create(company_id=company_id, project_id=project_id,
    #                                                content_id=content_type_id)
    #             created = True
    #
    #     if created:
    #         sequence.current_sequence = 1
    #     else:
    #         sequence.current_sequence = F('current_sequence') + 1
    #
    #     sequence.save()
    #     if 0:
    #         print(args)
    #     return Sequence.objects.get(pk=sequence.pk).current_sequence