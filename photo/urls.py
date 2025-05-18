from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<str:pk>/', views.viewPhoto, name='viewPhoto'),
    path('delete/<str:pk>/', views.deletePhoto, name='deletePhoto'),
    path('delete-category/<str:pk>/', views.delete_category, name='delete-category'),
    path('add/', views.addPhoto, name='add'),
]