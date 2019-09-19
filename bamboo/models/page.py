'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from bamboo.models.user import User

class Page(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        blank=True,
        null=True,
        max_length=128,
        default=''
    )
    body = models.TextField(
        verbose_name='本文',
        blank=True,
        null=True,
        max_length=10000,
    )
    status = models.IntegerField(
        verbose_name='公開状態',
        blank=True,
        null=True,
        default=0
    )

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

    users = models.ManyToManyField(
        User,
        through="UserPage",
    )

    notes = models.ManyToManyField(
        "Note",
        through="NotePage"
    )

    page_comments = models.ManyToManyField(
        "PageComment",
        through="PagePageComment"
    )

    def __str__(self):
        return str(self.id)
