from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer

from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Получает токен авторизации"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        # token['username'] = user.username
        token['email'] = user.email

        return token


class UserCreateSerializer(ModelSerializer):
    """Создаёт пользователя"""
    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])
        return new_user

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(ModelSerializer):
    """Смотрит список юзеров"""
    class Meta:

        model = User
        fields = '__all__'
