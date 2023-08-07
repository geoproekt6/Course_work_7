from django.urls import path

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, RegisterAPIView, ListUserAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('list/', ListUserAPIView.as_view(), name='userlist'),
]
