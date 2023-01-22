from django.contrib.gis.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from account.models import Client, Driver
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Client, Driver


class TripManager(models.Manager):
    def not_started_trips(self):
        return self.get_queryset().filter(
            Q(status="REQUESTED")
        )


class RequestDriverManager(models.Manager):
    def get_user_trip(self, driver_username):
        return self.get_queryset().filter(driver__user__username=driver_username)

    def can_delete_this_request(self, driver_username):
        trip_user = self.get_user_trip(driver_username)
        if trip_user:
            return trip_user.filter(
                (
                        Q(status="REQUESTED") |
                        Q(status="PROCESSED")
                ))

    def list_driver_is_ready_for_start(self):

        return self.get_queryset().filter(
            (
                    Q(status="REQUESTED") |
                    Q(status="PROCESSED") |
                    Q(status="COMPLETED") |
                    Q(status="CANCELLED")))

    def driver_can_add_request(self, driver_username):
        trip_user = self.get_user_trip(driver_username)
        if trip_user:
            return trip_user.filter(
                Q(status="STARTED") | Q(status="REQUESTED") | Q(
                    status="PROCESSED")).count() == 0  # have completed or cancelled or no request at all
        else:  # has not registered any request
            return True

    def driver_having_unfinished_trip(self, driver_username):
        """
        this driver cannot take any trip
        """
        trip_user = self.get_user_trip(driver_username)
        if trip_user:
            return trip_user.filter(
                (
                        Q(status="REQUESTED") |
                        Q(status="PROCESSED") |
                        Q(status="STARTED")))

    def list_ready_drivers(self):
        """
        drivers with no unfinished trips
        """
        return self.get_queryset().filter(
            (
                    Q(status="REQUESTED") |
                    Q(status="PROCESSED")
            ))


class RequestClientManager(models.Manager):
    def get_user_trip(self, passenger_username):
        return self.get_queryset().filter(client__user__username=passenger_username)

    def can_delete_this_request(self, passenger_username):
        trip_user = self.get_user_trip(passenger_username)
        if trip_user:
            return trip_user.filter(
                (
                        Q(status="REQUESTED") |
                        Q(status="PROCESSED")
                ))

    def passenger_having_unfinished_trip(self, passenger_username):
        trip_user = self.get_user_trip(passenger_username)
        if trip_user:
            return trip_user.filter(
                (
                        Q(status="REQUESTED") |
                        Q(status="PROCESSED") |
                        Q(status="STARTED")))

    def list_ready_passengers(self):
        """
        drivers with no unfinished trips
        """
        return self.get_queryset().filter(
            (
                    Q(status="REQUESTED") |
                    Q(status="PROCESSED")
            ))

    def list_passenger_list_ready_for_start(self):
        return self.get_queryset().filter(
            (
                    Q(status="REQUESTED") |
                    Q(status="PROCESSED") |
                    Q(status="COMPLETED") |
                    Q(status="CANCELLED")))

    def passenger_can_add_request(self, passenger_id):
        trip_user = self.get_user_trip(passenger_id)
        if trip_user:
            return trip_user.filter(
                Q(status="STARTED") |  Q(status="REQUESTED") | Q(
                    status="PROCESSED")).count() == 0  # have completed or cancelled or no request at all
        else:  # has not registered any request
            return True


REQUESTED = 'REQUESTED'
STARTED = 'STARTED'
CANCELLED = 'CANCELLED'
COMPLETED = 'COMPLETED'
PROCESSED = "PROCESSED"
STATUSES = (
    (REQUESTED, REQUESTED),
    (STARTED, STARTED),
    (CANCELLED, CANCELLED),
    (COMPLETED, COMPLETED),
    (PROCESSED, PROCESSED),
)


class Car(models.Model):
    driver = models.OneToOneField(
        verbose_name=_('راننده'), to=Driver, on_delete=models.CASCADE)
    color = models.CharField(_('رنگ'), max_length=30)
    model = models.DateField(_('مدل'))
    number_plate_first_part = models.CharField(_('پلاک قسمت 1'), max_length=2)
    number_plate_second_part = models.CharField(_('پلاک قسمت 2'), max_length=1)
    number_plate_third_part = models.CharField(_('پلاک قسمت 3'), max_length=3)
    number_plate_forth_part = models.CharField(_('پلاک قسمت 4'), max_length=2)
    type = models.CharField(max_length=255 , default = 'pride')
    def __str__(self):
        return f'car model {self.model} of {self.driver}'


class RequestDriver(models.Model):
    status = models.CharField(
        max_length=100, choices=STATUSES, default=REQUESTED
    )
    driver = models.ForeignKey(
        verbose_name=_('راننده'),
        to=Driver, on_delete=models.CASCADE, null=True, blank=True,
        related_name='driver_of_request'
    )
    req_start = models.DateTimeField(
        _('تاریخ شروع درخواست'), auto_now_add=True)
    start_loc = models.PointField(_('مکان ثبت'))
    distance = models.FloatField(_('مسافت'), null=True, blank=True)
    estimated_time = models.PositiveBigIntegerField(
        _('زمان تخمینی'), null=True, blank=True)
    start_loc_lat = models.FloatField(_('عرض شروع'), null=True, blank=True)
    start_loc_lon = models.FloatField(_('طول شروع'), null=True, blank=True)
    finish_loc_lat = models.FloatField(_('عرض پایان'), null=True, blank=True)
    finish_loc_lon = models.FloatField(_('طول پایان'), null=True, blank=True)
    objects = RequestDriverManager()

    def __str__(self):
        return self.driver.user.username


class RequestClient(models.Model):
    status = models.CharField(
        max_length=100, choices=STATUSES, default=REQUESTED
    )
    client = models.ForeignKey(
        verbose_name=_('کاربر'), to=Client, on_delete=models.CASCADE,
        null=True, blank=True, related_name='client_of_request')
    req_start = models.DateField(_('تاریخ شروع درخواست'), auto_now_add=True)
    req_time_start = models.TimeField(
        _('تاریخ شروع درخواست'), auto_now_add=True)
    start_loc = models.PointField(_('مکان ثبت'), )
    finish_loc = models.PointField(_('مکان نهایی'), null=True, blank=True)
    distance = models.FloatField(_('مسافت'), null=True, blank=True)
    estimated_time = models.PositiveBigIntegerField(
        _('زمان تخمینی'), null=True, blank=True)
    start_loc_lat = models.FloatField(_('عرض شروع'), null=True, blank=True)
    start_loc_lon = models.FloatField(_('طول شروع'), null=True, blank=True)
    finish_loc_lat = models.FloatField(_('عرض پایان'), null=True, blank=True)
    finish_loc_lon = models.FloatField(_('طول پایان'), null=True, blank=True)
    text_address_start = models.TextField(verbose_name=_(' آدرس مبدا'), null=True, blank=True)
    text_address_finish = models.TextField(verbose_name=_('آدرس مقصد'), null=True, blank=True)
    objects = RequestClientManager()

    def __str__(self):
        return self.client.user.username


class Trip(models.Model):
    """
    Trip model
    """
    status = models.CharField(
        max_length=100, choices=STATUSES, default=REQUESTED
    )
    distance = models.FloatField(_('مسافت'))
    start_time = models.DateTimeField(_('تاریخ حرکت'), null=True, blank=True)
    finish_time = models.DateTimeField(_('تاریخ رسیدن'), null=True, blank=True)
    driver = models.ForeignKey(verbose_name=_(
        'راننده'), to=Driver, on_delete=models.CASCADE, related_name='driver_trip', null=True, blank=True)
    passenger = models.ForeignKey(verbose_name=_(
        'مسافر'), to=Client, on_delete=models.CASCADE, related_name='passenger_trip', null=True, blank=True)
    req_driver = models.ForeignKey(RequestDriver, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='driver_request_trip')
    req_passenger = models.ForeignKey(RequestClient, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='client_request_trip')
    objects = TripManager()

    def __str__(self):
        return f'{self.driver.user.username} riding {self.passenger.user.username}'
# @receiver(post_save, sender=RequestClient)
# def notify_driver_new_trip(sender, instance, created, **kwargs):
#     if created:
#         print('a passenger has requested a trip')
#         ready_drivers = RequestDriver.objects.filter(status="REQUESTED")
#         if ready_drivers:
#             for d in ready_drivers:
#                 dis = distance(d.start_loc_lat, instance.start_loc_lat,
#                                d.start_loc_lon, instance.start_loc_lon)
#                 if dis < 2:
#                     Trip.objects.create(
#                         distance = instance.distance ,
#                         driver = d.driver,
#                         passenger = instance.client,
#                     )
#                     user = User.object.get(username = d.driver.uesrname)
#                 send_user_notification(user=user, payload=payload, ttl=1000)
