from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habbits
from users.models import User


class ViewTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='dronramone@mail.ru',
            password='password123',
            is_superuser=True,
            tg_login="Blendis",
        )
        self.client.force_authenticate(user=self.user)

        habit = Habbits.objects.create(
                id=46,
                place="Кухня",
                times="00:00",
                action="Гулять",
                good_habit_sign=False,
                periodicity=2,
                reward='',
                execution_time='00:01:00',
                is_public=False,
                user=self.user,
                relted_habbit=None
        )
        habit.save()

    def test_list_habbit(self):
        responce = self.client.get(
                '/habbits/',
            )
        print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
