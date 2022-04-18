from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateQuote.as_view(), name='index'),
    path('quote/<int:pk>', views.QuoteDetailView.as_view(), name='quote'),
    ]
