from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/', views.author_page, name='card_author')
]