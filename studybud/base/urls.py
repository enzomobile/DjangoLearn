# Urls for the app
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('room/<str:pk>/', views.room, name='room'),  # Room page
]