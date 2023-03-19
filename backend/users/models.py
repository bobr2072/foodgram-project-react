from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subscriber',
        verbose_name='Подписывающийся юзер',
    )
    author_sub = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='author_sub',
        verbose_name='Автор, на которого подписываются',
    )

    class Meta:
        verbose_name = 'Подписки на авторов'
        unique_together = ['subscriber', 'author_sub']
        constraints = [
            models.UniqueConstraint(
                fields=['subscriber', 'author_sub'],
                name='unique_subscription'
            )
        ]
