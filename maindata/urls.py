from django.contrib import admin
from django.urls import include, path

from maindata.views import getselectedclientaddress,invoice

# from .views import getfromclientid
app_name = 'maindata'

urlpatterns = [
    path('invoice/<int:pk>/', invoice, name="invoice"),
    path('getselectedclientaddress/<int:pk>/', getselectedclientaddress, name='getselectedclientaddress'),
]



