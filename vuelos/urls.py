from django.urls import path
from .views import *

urlpatterns =[
    path("",HomePageView.as_view(), name='home'),
    path('flights/',FlightListView.as_view(),name='index'),
    path('register/',FlightCreateView.as_view(),name='form'),
    path('stats/',FlightStatisticsView.as_view(),name='stats'),
]