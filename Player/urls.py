from django.urls import path, include
from rest_framework import routers
from django.http import HttpResponse


from . import api
from . import views


router = routers.DefaultRouter()

urlpatterns = (
    # Call the get_random_station function from Views.py
    path('', views.get_random_station, name='station'),
    
)
