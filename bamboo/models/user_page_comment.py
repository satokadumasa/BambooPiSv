'''
Created on 2019/09/16

@author: satoukentadashi
'''
from django.db import models
from django.utils import timezone
from bamboo.models.page_comment import PageComment
from bamboo.models.user import User

class UserPageComment(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    page_comment = models.ForeignKey(PageComment, verbose_name='ページコメント', on_delete=models.CASCADE)

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
