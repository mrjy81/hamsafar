from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from main.models import RequestClient, RequestDriver, Trip
from main.login_decorator import login_driver, login_passenger
from account.models import Driver, Client
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.db.models import Q
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from main.login_decorator import login_passenger
from .form import ChargeForm
from django.utils import timezone


@login_passenger
def go_to_gateway_view(request, value):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = value
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    # user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse('callback-gateway'))
        # bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        user = Client.objects.get(user=request.user)
        user.charge += int(bank_record.amount)
        user.save()
        return redirect('charge')

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


@login_driver
def driver_workflow(request):
    driver = Driver.objects.get(user=request.user)
    try:
        req = RequestDriver.objects.driver_having_unfinished_trip(driver.user.username).first()
        if req is None:
            raise 'is none'
    except Exception as e:
        result = {'message': 'شما درخواستی ثبت نکرده اید',
                  'flag': False,
                  }
    else:
        result = {'start_lat': req.start_loc_lat, "start_lon": req.start_loc_lon,
                  "finish_lon": req.finish_loc_lon, "finish_lat": req.finish_loc_lat,
                  "flag": True,
                  }
        if req.status == "STARTED":
            trip_id = Trip.objects.get(
                status="STARTED",
                req_driver=req
            )
            result['trip_id'] = trip_id.id
    context = {
        'loc': result,
    }
    return render(request, 'd.html', context)


@login_passenger
def passenger_workflow(request):
    user = Client.objects.get(user=request.user)
    try:
        req = RequestClient.objects.passenger_having_unfinished_trip(user.user.username).first()
        if req is None:
            raise 'is none'
    except:
        result = {'message': 'شما درخواستی ثبت نکرده اید',
                  'flag': False,
                  }
    else:
        result = {'start_lat': req.start_loc_lat,
                  "start_lon": req.start_loc_lon,
                  "finish_lon": req.finish_loc_lon,
                  "finish_lat": req.finish_loc_lat,
                  "flag": True,
                  }
    context = {
        'loc': result,
    }
    return render(request, 'p.html', context)


@login_passenger
def del_passenger(request):
    """
         handle client request to change status to cancelled
    """
    user = Client.objects.get(user=request.user)
    cancelled_request = RequestClient.objects.can_delete_this_request(user.user.username).first()
    if cancelled_request is not None:
        cancelled_request.status = "CANCELLED"
        cancelled_request.save()

    trip = Trip.objects.not_started_trips().filter(req_passenger=cancelled_request).first()
    if trip is not None:
        trip.status = "CANCELLED"
        trip.req_passenger.status = "REQUESTED"
        trip.save()
    return redirect('passenger-dashboard')


@login_driver
def del_driver(request):
    user = Driver.objects.get(user=request.user)
    cancelled_request = RequestDriver.objects.can_delete_this_request(user.user.username)
    if cancelled_request is not None:
        cancelled_request.status = "CANCELLED"
        cancelled_request.save()
    trip = Trip.objects.not_started_trips().filter(req_driver=cancelled_request).first()
    if trip is not None:
        trip.status = "CANCELLED"
        # req_updated = RequestClient.objects.get(client_request_trip=)
        trip.req_passenger.status = "REQUESTED"
        trip.req_passenger.save()
        trip.save()
    return redirect('driver-dashboard')


def get_driver_trip(request):
    user = Driver.objects.get(user=request.user)
    trip = Trip.objects.filter(driver=user, status='REQUESTED').select_related(
        'req_passenger_id').values()
    data = {}

    for i in trip:
        req = RequestClient.objects.get(id=i['req_passenger_id'])
        data[i['id']] = {"status": i['status'],
                         "distance": i['distance'],
                         "passenger": i['passenger_id'],
                         "start_address": req.text_address_start,
                         "finish_address": req.text_address_finish,
                         'id': i['id'],
                         }
    return JsonResponse(data)


@login_driver
def accept_trip(request, trip_id):
    if RequestDriver.objects.filter(
            Q(driver__user__username=request.user.username) &
            ~Q(status="STARTED")):
        trip = get_object_or_404(Trip, id=int(trip_id))
        driver = Driver.objects.get(user=request.user)
        passenger_req = trip.req_passenger
        driver_req = trip.req_driver
        org_lat = trip.req_passenger.start_loc_lat
        org_lon = trip.req_passenger.start_loc_lon
        des_lat = trip.req_passenger.finish_loc_lat
        des_lon = trip.req_passenger.finish_loc_lon
        if trip.driver == driver:
            trip.status = "STARTED"
            passenger_req.status = "STARTED"
            driver_req.status = "STARTED"
            trip.start_time = timezone.now()
            trip.save()
            passenger_req.save()
            driver_req.save()
            return redirect(
                f'https://neshan.org/maps/@35.671030,51.324759,14.7z,0.0p/routing/car/origin/{org_lat},{org_lon}/destination/{des_lat},{des_lon}')
    else:
        return HttpResponse('شما سفر در حال انجام دارید')


@login_passenger
def charge_view(request):
    form = ChargeForm()
    user = Client.objects.get(user=request.user)
    if request.method == "POST":
        form = ChargeForm(request.POST or None)
        if form.is_valid():
            value = form.cleaned_data['value']
            return redirect('go-to-gate-way', value=value)
    context = {
        'form': form,
        'money': user.charge
    }
    return render(request, 'charge.html', context)


def successful_trip_view(request, trip_id):
    trip = get_object_or_404(Trip, id=int(trip_id))
    driver = Driver.objects.get(user=request.user)
    passenger_req = trip.req_passenger
    driver_req = trip.req_driver
    if trip.driver == driver:
        trip.status = "COMPLETED"
        passenger_req.status = "COMPLETED"
        driver_req.status = "COMPLETED"
        passenger_req.client.charge -= (passenger_req.estimated_time / 60) * 5000
        trip.finish_time = timezone.now()
        trip.save()
        passenger_req.save()
        driver_req.save()
        passenger_req.client.save()
    return redirect('home')
