'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from bamboo.models.album import Album
from bamboo.models.attachment import Attachment

class AlbumAttachment(models.Model):
    album = models.ForeignKey(Album, verbose_name='アルバム', on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name='添付ファイル', on_delete=models.CASCADE)

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
