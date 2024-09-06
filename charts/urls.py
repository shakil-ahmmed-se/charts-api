from django.urls import path
from . import views

urlpatterns = [
    path('candleChart/', views.candleChart, name='candleChart'),
    path('lineChart/', views.lineChart, name='lineChart'),
    path('barChart/', views.barChart, name='barChart'),
    path('pieChart/', views.pieChart, name='pieChart'),
]
