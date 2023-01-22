from django.contrib import admin
from .models import Car, Trip, RequestDriver, RequestClient
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.contrib.gis.admin import OSMGeoAdmin
import django_jalali.admin as jadmin


@admin.register(Car)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['model', 'driver', 'color', 'number_plate']

    def number_plate(self, obj):
        return f'{obj.number_plate_first_part} {obj.number_plate_second_part} {obj.number_plate_third_part} ایران {obj.number_plate_forth_part}'

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


@admin.register(Trip)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['distance', 'passenger', 'driver','status']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


@admin.register(RequestDriver)
class FirstModelAdmin(OSMGeoAdmin, ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['status', 'req_start', 'driver']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


@admin.register(RequestClient)
class FirstModelAdmin(OSMGeoAdmin, ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['status', 'req_start', 'client']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'
