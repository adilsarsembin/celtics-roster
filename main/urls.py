from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('players/', views.players, name='players'),
    path('players/<str:pk>', views.one_player, name='one_player')
]
