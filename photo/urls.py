from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:pk>/', views.viewPhoto, name='viewPhoto'),
    path('add/', views.addPhoto, name='add'),
]