'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class SiteUser(models.Model):
    site = models.ForeignKey(Site, verbose_name='サイト', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='ユーザ', on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        verbose_name='作成日時',
        blank=True,
        null=True,
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        blank=True,
        null=True,
        default=timezone.now
    )

    deleted_at = models.DateTimeField(
        verbose_name='削除日時',
        blank=True,
        null=True,
        default=timezone.now
    )
