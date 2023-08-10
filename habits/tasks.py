from celery import shared_task
from django.utils.timezone import now

from habits.models import Habbits
from telegramm.bot import TeleBotApi


@shared_task
def send_message():
    queryset = Habbits.objects.all()
    for habit in queryset:
        if habit.times.strftime("%H:%M") == now().strftime("%H:%M"):
            datas = {
                'action': habit.action,
                'times': habit.times,
                'place': habit.place,
            }
            TeleBotApi.send_message(**datas)
