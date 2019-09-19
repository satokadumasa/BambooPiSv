'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone

class Site(models.Model):
    site_name = models.CharField(
        verbose_name='サイト名',
        blank=True,
        null=True,
        max_length=128,
        default=''
    )
    host_name = models.CharField(
        verbose_name='ホスト名',
        blank=True,
        null=True,
        max_length=128,
        default=''
    )
    port = models.IntegerField(
        verbose_name='公開ポート番号',
        blank=True,
        null=True,
        default=0
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

    rooms = models.ManyToManyField(
        "User",
        through="SiteUser",
#         through_fields=("user_id","note_id")
    )

    users = models.ManyToManyField(
        "Room",
        through="SiteRoom",
#         through_fields=("user_id","note_id")
    )

    def __str__(self):
        return str(self.id)
