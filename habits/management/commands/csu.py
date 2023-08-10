from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='dronramone@mail.ru',
            first_name='Blendi',
            last_name='Inc',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('188651')
        user.save()
