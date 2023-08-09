from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabbitsCreateAPIView, HabbitsListAPIView, HabbitsDetailAPIView, HabbitsUpdatelAPIView, \
    HabbitsDeleteAPIView, HabbitsPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabbitsCreateAPIView.as_view(), name='habbits_create'),
    path('', HabbitsListAPIView.as_view(), name='habbits_list'),
    path('<int:pk>/', HabbitsDetailAPIView.as_view(), name='habbits_detail'),
    path('update/<int:pk>/', HabbitsUpdatelAPIView.as_view(), name='habbits_update'),
    path('delete/<int:pk>/', HabbitsDeleteAPIView.as_view(), name='habbits_delete'),

    path('public/', HabbitsPublicListAPIView.as_view(), name='public_habbits_list'),
]
