from django.urls import path
from .views import *

urlpatterns =[
    path("",HomePageView.as_view(), name='home'),
    path('flights/',FlightListView.as_view(),name='index'),
    path('flights/register/',FlightCreateView.as_view(),name='form'),
    #path('products/',ProductIndexView.as_view(),name='index'),
]