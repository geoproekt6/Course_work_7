from rest_framework.serializers import ModelSerializer

from habits.models import Habbits


class HabbitsCreateSerializer(ModelSerializer):
    """"""

    class Meta:
        model = Habbits
        fields = '__all__'
