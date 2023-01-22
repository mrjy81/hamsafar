from account.models import Client, Driver
from django.shortcuts import HttpResponse, redirect


def login_driver(driver_view):
    def is_driver(request, *args, **kwargs):
        if request.user.is_authenticated:
            if Driver.objects.filter(user=request.user).first():
                return driver_view(request, *args, **kwargs)
            else:
                return redirect('login-driver')
        else:
            return redirect('register-driver')

    return is_driver


def login_passenger(passenger_view):
    def is_passenger(request, *args, **kwargs):
        if request.user.is_authenticated:
            if Client.objects.filter(user=request.user).first():
                return passenger_view(request, *args, **kwargs)
            else:
                return redirect('login-passenger')
        else:
            return redirect('register-passenger')

    return is_passenger
