from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetIndexPage, name='index'),
    ]
