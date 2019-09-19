'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from bamboo.models.note import Note
from bamboo.models.page import Page

class NotePage(models.Model):
    note = models.ForeignKey(Note, verbose_name='ノート', on_delete=models.CASCADE)
    page = models.ForeignKey(Page, verbose_name='ページ', on_delete=models.CASCADE)

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

    def __str__(self):
        return self.id
