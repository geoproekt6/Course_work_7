from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import validators

from habits.models import Habbits
from users.validators import TogetherValidators, TimeValidators


class HabbitsCreateSerializer(ModelSerializer):
    """"""

    class Meta:
        model = Habbits
        fields = '__all__'
        validators = [
            TogetherValidators(),
            TimeValidators(),
        ]


class HabbitslistSerializer(ModelSerializer):
    """"""
    user = SerializerMethodField()

    @staticmethod
    def get_user(instance):
        return instance.user.email

    class Meta:
        model = Habbits
        fields = '__all__'
