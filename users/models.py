from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    tg_login = models.CharField(max_length=127, **NULLABLE, verbose_name='Логин в телеграме')
    chat_id = models.CharField(max_length=127, **NULLABLE, verbose_name='ID чата в телеграме')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}, {self.tg_login}, {self.chat_id}, {self.is_active}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
