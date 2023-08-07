from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserCreateSerializer, UserListSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
