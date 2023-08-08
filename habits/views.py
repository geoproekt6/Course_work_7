from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habbits


# Create your views here.

class HabbitsCreateAPIView(CreateAPIView):
    """"""
    serializer_class = ...

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsListAPIView(ListAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsDetailAPIView(RetrieveAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsUpdatelAPIView(UpdateAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsDeleteAPIView(DestroyAPIView):
    """"""
    queryset = Habbits.objects.all()

    class Meta:
        model = Habbits
        fields = '__all__'
