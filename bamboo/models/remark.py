'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone

class Remark(models.Model):
    body = models.TextField(
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

    rooms = models.ManyToManyField(
        "Room",
        through="RoomRemark",
#         through_fields=("user_id","note_id")
    )

    users = models.ManyToManyField(
        "User",
        through="UserRemark",
#         through_fields=("user_id","note_id")
    )
