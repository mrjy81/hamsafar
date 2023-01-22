from django.urls import path
from . import views

urlpatterns = [
    path('driver-wf', views.driver_workflow, name='driver-wf'),
    path('passenger-wf', views.passenger_workflow, name='passenger-wf'),
    path('del-p', views.del_passenger, name='delete-req-passenger'),
    path('del-d', views.del_driver, name='delete-req-driver'),
    path('trip-d', views.get_driver_trip, name='driver-trip'),
    path('go-to-gate-way/<int:value>', views.go_to_gateway_view, name='go-to-gate-way'),
    path('callback-gateway', views.callback_gateway_view, name='callback-gateway'),
    path('accept-trip/<str:trip_id>/', views.accept_trip, name='accept-trip'),
    path('charge-account', views.charge_view, name='charge'),
    path('success-trip/<int:trip_id>', views.successful_trip_view, name='success-trip'),

]
