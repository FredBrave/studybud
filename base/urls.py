from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('room/<str:id>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create-room'),
    path('update_room/<str:id>', views.updateRoom, name='update-room'),
    path('delete_room/<str:id>', views.deleteRoom, name='delete-room'),

]