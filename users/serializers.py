from rest_framework.serializers import ModelSerializer

from users.models import User


class UserCreateSerializer(ModelSerializer):
    """Создаёт пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(ModelSerializer):
    """Смотрит список юзеров"""
    class Meta:

        model = User
        fields = '__all__'
