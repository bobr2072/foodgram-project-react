from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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
        ordering = ('-id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписывающийся юзер',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Автор, на которого подписываются',
    )

    class Meta:
        verbose_name = 'Подписки на авторов'
        unique_together = ('user', 'author')
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            )
        ]

    def validate_subscription(self):
        if self.user == self.author:
            raise ValidationError('User cannot subscribe to themselves.')
