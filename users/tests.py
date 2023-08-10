from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_user(self):
        responce = self.client.post(
                '/users/register/',
                data={
                    "password": '123qwe456ert',
                    "email": "blendi@mail.ru"
                }
            )
        print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
