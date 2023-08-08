from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserCreateSerializer, UserListSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class DeleteUserAPIView(DestroyAPIView):
    queryset = User.objects.all()
