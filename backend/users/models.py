from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subcribe(models.Model):
    user_following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='follower',
        verbose_name='Подписывающийся юзер',
    )
    author_followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='following',
        verbose_name='Автор, на которого подписываются',
    )

    class Meta:
        verbose_name = 'Подписки на авторов'
        unique_together = ['user_following', 'author_followed']
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user_following=models.F('author_followed')),
                name='no_self_follows'
            )
        ]
