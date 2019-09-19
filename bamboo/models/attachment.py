'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone

class Attachment(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        blank=True,
        null=True,
        max_length=128,
        default=''
    )
    description = models.TextField(
        verbose_name='説明文',
        blank=True,
        null=True,
        max_length=1000,
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

    albums = models.ManyToManyField(
        "Album",
        through="AlbumAttachment",
#         through_fields=("user_id","note_id")
    )

    def __str__(self):
        return self.id
