from datetime import datetime, time, timedelta

from rest_framework.serializers import ValidationError

from habits.models import Habbits


class TogetherValidators:

    def __call__(self, value):

        if value['reward'] is not None and value['relted_habbit'] is not None:
            raise ValidationError(
                'Выберите что-то одно, либо вознаграждение, либо приятность'
            )


class TimeValidators:

    def __call__(self, value):
        time_object = value['execution_time']
        seconds = timedelta(hours=time_object.hour, minutes=time_object.minute,
                            seconds=time_object.second).total_seconds()

        if seconds > 120:
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд'
            )



class IsNice:

    def __call__(self, value):
        if value['relted_habbit'].good_habit_sign is False:
            raise ValidationError(
                "Приятной привычкой может быть только приятная привычка"
            )
