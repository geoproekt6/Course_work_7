from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.apps import UsersConfig
from users.views import RegisterAPIView, ListUserAPIView, DeleteUserAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('list/', ListUserAPIView.as_view(), name='userlist'),
    path('delete/<int:pk>/', DeleteUserAPIView.as_view(), name='userdelete'),
]
