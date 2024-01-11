from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('create/', views.ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete'),
]