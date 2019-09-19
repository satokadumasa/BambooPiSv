'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from bamboo.models.room import Room
from bamboo.models.remark import Remark

class RoomRemark(models.Model):
    room = models.ForeignKey(Room, verbose_name='ルーム', on_delete=models.CASCADE)
    remark = models.ForeignKey(Remark, verbose_name='発言', on_delete=models.CASCADE)

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
        return str(self.id)
