from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habbits
from habits.serializers import HabbitsCreateSerializer


# Create your views here.

class HabbitsCreateAPIView(CreateAPIView):
    """"""
    serializer_class = HabbitsCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request)

        new_habbit = Habbits.objects.create()

        return new_habbit

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsListAPIView(ListAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsDetailAPIView(RetrieveAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsUpdatelAPIView(UpdateAPIView):
    """"""
    queryset = Habbits.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsDeleteAPIView(DestroyAPIView):
    """"""
    queryset = Habbits.objects.all()
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Habbits
        fields = '__all__'
