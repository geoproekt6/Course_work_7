from django.conf import settings
from django.db import models
from users.models import User, NULLABLE


class Habbits(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='создатель привычки',
    )
    place = models.CharField(max_length=127, verbose_name='место выполнения')
    times = models.TimeField(default='00:00', verbose_name='время начала выполнения')
    action = models.CharField(max_length=127, verbose_name='действие')
    good_habit_sign = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    relted_habbit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='связанная привычка'
    )
    periodicity = models.IntegerField(verbose_name='периодичность')
    reward = models.CharField(max_length=127, verbose_name='вознаграждение', **NULLABLE)
    execution_time = models.TimeField(default='00:02', verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.user}, {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ['times']
