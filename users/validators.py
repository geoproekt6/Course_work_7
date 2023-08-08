from datetime import datetime, time, timedelta

from rest_framework.serializers import ValidationError


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

