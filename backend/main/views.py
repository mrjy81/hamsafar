from django.shortcuts import render, redirect
from .form import PassengerGeoForm, DriverGeoForm
from .models import RequestClient, RequestDriver, Trip
from account.models import Client, Driver
from .login_decorator import login_driver, login_passenger
from django.http import JsonResponse
from django.contrib.gis.geos import fromstr
from .distance import distance_calc
from webpush import send_user_notification
from django.db.models import Q
from django.db import transaction
from django.contrib.auth import get_user_model
import json

User = get_user_model()


def home(request):
    context = {}
    return render(request, 'home.html', context)


@login_passenger
def passenger_dashboard_view(request):
    """
    passenger can add a location hope any driver accept it
    """
    user = Client.objects.get(user=request.user)
    if not RequestClient.objects.passenger_can_add_request(user.user.username):
        return redirect('passenger-wf')
    if request.method == "POST":
        data_info = json.loads(request.POST['dis'])
        data = json.loads(request.POST['loc'])
        address = json.loads(request.POST['addresses'])
        estimated_time = float(
            data_info['rows'][0]['elements'][0]['duration']['value'])
        distance = data_info['rows'][0]['elements'][0]['distance']['value']
        start_loc_lat = float(data[0]["lat"])
        start_loc_lon = float(data[0]["lon"])
        finish_loc_lat = float(data[1]["lat"])
        finish_loc_lon = float(data[1]["lon"])
        # hasn't unfinished request
        price = (estimated_time / 60) * 5000
        if user.charge >= price:
            with transaction.atomic():
                req = RequestClient.objects.create(
                    client=user,
                    start_loc=fromstr(
                        f'POINT({start_loc_lon} {start_loc_lat})', srid=4326),
                    finish_loc=fromstr(
                        f'POINT({finish_loc_lon} {finish_loc_lat})', srid=4326),
                    estimated_time=estimated_time,
                    distance=distance,
                    start_loc_lat=start_loc_lat,
                    start_loc_lon=start_loc_lon,
                    finish_loc_lat=finish_loc_lat,
                    finish_loc_lon=finish_loc_lon,
                    text_address_start=address['start_address'],
                    text_address_finish=address['finish_address'],
                )
                ready_drivers = RequestDriver.objects.list_driver_is_ready_for_start()  # avaliable driver
                if ready_drivers:
                    for d in ready_drivers:
                        dis_start = distance_calc(d.start_loc_lat, req.start_loc_lat,
                                                  d.start_loc_lon, req.start_loc_lon)
                        dis_finish = distance_calc(d.finish_loc_lat, req.finish_loc_lat,
                                                   d.finish_loc_lon, req.finish_loc_lon)
                        if dis_start < 5 and dis_finish < 5:
                            Trip.objects.create(
                                distance=req.distance,
                                driver=d.driver,
                                passenger=req.client,
                                req_passenger=req,
                                req_driver=d,
                            )
                            d.status = "PROCESSED"
                            req.status = "PROCESSED"
                            req.save()
                            d.save()
        else:
            return redirect('charge')
        return JsonResponse({'ok': 'status'})

    context = {}
    return render(request, 'pd.html', context)


@login_driver
def driver_dashboard_view(request):
    user = Driver.objects.get(user=request.user)
    if not RequestDriver.objects.driver_can_add_request(user.user.username):
        return redirect('driver-wf')
    elif request.method == "POST":
        data = json.loads(request.POST['loc'])
        start_loc_lat = float(data[0]["lat"])
        start_loc_lon = float(data[0]["lon"])
        finish_loc_lat = float(data[1]["lat"])
        finish_loc_lon = float(data[1]["lon"])
        # hasn't unfinished request
        with transaction.atomic():
            req = RequestDriver.objects.create(
                driver=user,
                start_loc=fromstr(
                    f'POINT({start_loc_lon} {start_loc_lat})', srid=4326),
                start_loc_lat=start_loc_lat,
                start_loc_lon=start_loc_lon,
                finish_loc_lat=finish_loc_lat,
                finish_loc_lon=finish_loc_lon,
            )

            ready_passenger = RequestClient.objects.list_passenger_list_ready_for_start()

            if ready_passenger:
                for p in ready_passenger:
                    dis_start = distance_calc(p.start_loc_lat, req.start_loc_lat,
                                              p.start_loc_lon, req.start_loc_lon)
                    dis_finish = distance_calc(p.finish_loc_lat, req.finish_loc_lat,
                                               p.finish_loc_lon, req.finish_loc_lon)
                    if dis_start < 5 and dis_finish < 5:
                        Trip.objects.create(
                            distance=p.distance,
                            driver=req.driver,
                            passenger=p.client,
                            req_passenger=p,
                            req_driver=req,
                        )
                        p.status = "PROCESSED"
                        req.status = "PROCESSED"
                        req.save()
                        p.save()
            return JsonResponse({'ok': 'status'})
    context = {}
    return render(request, 'dd.html', context)
