from datetime import datetime, time, timedelta

from rest_framework.serializers import ValidationError

from habits.models import Habbits


class TogetherValidators:
    """Исключить одновременный выбор связанной привычки и указания вознаграждения."""
    def __call__(self, value):

        if value['good_habit_sign'] is False:

            if value['reward'] is not None and value['relted_habbit'] is not None:
                raise ValidationError(
                    'Выберите что-то одно, либо вознаграждение, либо приятность'
                )
            elif value['reward'] is None and value['relted_habbit'] is None:
                raise ValidationError(
                    'Выберите себе хоть какую-нибудь награду'
                )


class TimeValidators:
    """Время выполнения должно быть не больше 120 секунд"""
    def __call__(self, value):
        time_object = value['execution_time']
        seconds = timedelta(hours=time_object.hour, minutes=time_object.minute,
                            seconds=time_object.second).total_seconds()

        if seconds > 120:
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд'
            )


class IsNice:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""
    def __call__(self, value):
        if value['relted_habbit'] is not None and value['relted_habbit'].good_habit_sign is False:
            raise ValidationError(
                "Приятной привычкой может быть только приятная привычка"
            )


class NiceNoReward:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""
    def __call__(self, value):
        if value['good_habit_sign']:
            if value['relted_habbit'] is not None:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки"
                )
            elif value['reward'] is not None:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения"
                )
