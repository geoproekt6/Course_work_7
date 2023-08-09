from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habbits
from habits.pagination import MabbitsPaginator
from habits.permissions import OwnerOrSuperUser
from habits.serializers import HabbitsCreateSerializer, HabbitslistSerializer


# Create your views here.

class HabbitsCreateAPIView(CreateAPIView):
    """"""
    serializer_class = HabbitsCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        datas = request.data
        datas['user'] = self.request.user.id
        serializer = self.serializer_class(data=datas)

        if serializer.is_valid():
            habbit = serializer.save()
            habbit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsListAPIView(ListAPIView):
    """Список привычек"""
    serializer_class = HabbitslistSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MabbitsPaginator

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Habbits.objects.all()
        return Habbits.objects.filter(user=self.request.user)

    class Meta:
        model = Habbits
        fields = '__all__'


class HabbitsDetailAPIView(RetrieveAPIView):
    """"""
    # queryset = Habbits.objects.all()
    serializer_class = HabbitslistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Habbits.objects.all()
        return Habbits.objects.filter(user=self.request.user)

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


class HabbitsPublicListAPIView(ListAPIView):
    """Список публичных привычек"""
    queryset = Habbits.objects.filter(is_public=False)
    serializer_class = HabbitslistSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MabbitsPaginator

    class Meta:
        model = Habbits
        fields = '__all__'

