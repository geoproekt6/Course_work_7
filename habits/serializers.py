from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from habits.models import Habbits
from users.validators import (
    TogetherValidators,
    TimeValidators,
    IsNice,
    NiceNoReward
)


class HabbitsCreateSerializer(ModelSerializer):
    """"""

    class Meta:
        model = Habbits
        fields = '__all__'
        validators = [
            TogetherValidators(),
            TimeValidators(),
            IsNice(),
            NiceNoReward(),
        ]


class HabbitsDetailSerializer(ModelSerializer):
    """"""
    user = SerializerMethodField()
    relted_habbit = SerializerMethodField()

    @staticmethod
    def get_relted_habbit(instance):
        nice_habbit = Habbits.objects.get(id=instance.relted_habbit.id)
        return nice_habbit.action

    @staticmethod
    def get_user(instance):
        return instance.user.email

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsListSerializer(ModelSerializer):
    """"""
    user = SerializerMethodField()
    relted_habbit = SerializerMethodField()

    @staticmethod
    def get_relted_habbit(instance):
        if instance.relted_habbit is not None:
            nice_habbit = Habbits.objects.get(id=instance.relted_habbit.id)
            return nice_habbit.action
        return None

    @staticmethod
    def get_user(instance):
        return instance.user.email

    class Meta:
        model = Habbits
        fields = '__all__'
