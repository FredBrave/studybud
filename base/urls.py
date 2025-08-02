from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:id>/', views.room, name='room'),
]