from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pd', views.passenger_dashboard_view, name='passenger-dashboard'),
    path('dd', views.driver_dashboard_view, name='driver-dashboard'),
]