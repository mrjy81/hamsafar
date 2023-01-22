from django.shortcuts import render, redirect
from .forms import PassengerRegistrationForm, LoginForm, DriverRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from account.models import Client, Driver, Phones
from django.shortcuts import HttpResponse
from django.db import transaction
from django.contrib.auth.hashers import make_password

User = get_user_model()


def logout_view(request):
    logout(request)
    return redirect('home')


def login_driver(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if Driver.objects.filter(user=user).first():
                    login(request, user)
                    return redirect('driver-dashboard')
                else:
                    form.add_error(field='username', error=[
                        'مطمینی راننده ای؟'])
            else:
                form.add_error(field='username', error=[
                    'نام کاربری یا رمز عبور نادرست'])
    context = {
        'form': form,
    }
    return render(request, 'driver_login.html', context)


def login_passenger(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if Client.objects.filter(user=user).first():
                    login(request, user)
                    return redirect('passenger-dashboard')
                else:
                    form.add_error(field='username', error=[
                        'مطمينی مسافری ؟?'])
            else:
                form.add_error(field='username', error=[
                    'نام کاربری یا رمز عبور نادرست'])

    context = {
        'form': form,
    }
    return render(request, 'passenger_login.html', context)


def register_passenger(request):
    form = PassengerRegistrationForm()
    if request.user.is_authenticated:
        if Client.objects.filter(user=request.user).first():
            return redirect('passenger-dashboard')
    if request.method == "POST":
        form = PassengerRegistrationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            with transaction.atomic():
                user = User.objects.create(
                    username=username, password=make_password(password))
                ph = Phones.objects.create(phone=phone)
                Client.objects.create(user=user, phone=ph)
                return redirect('login-passenger')
    context = {'form': form}
    return render(request, 'passenger_register.html', context)


def register_driver(request):
    form = DriverRegistrationForm()
    if request.user.is_authenticated:
        if Driver.objects.filter(user=request.user).first():
            return redirect('driver-dashboard')
    if request.method == "POST":
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            with transaction.atomic():
                user = User.objects.create(
                    username=username, password=make_password(password))
                ph = Phones.objects.create(phone=phone)
                Driver.objects.create(user=user, phone=ph)
                return redirect('login-driver')

    context = {'form': form}
    return render(request, 'driver_registration.html', context)
