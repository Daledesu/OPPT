from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.mainpage, name="mainpage"),
    path('index/',views.index, name="index"),
    path('delete/<int:sid>/',views.delete, name = "delete"),
    path('update/<int:sid>/',views.update, name = "update"),
    path('edit/<int:sid>/',views.edit, name = "edit"),
    path('about/', views.about, name="about"),
    path('data/', views.Data, name="data"),
    ]