from django.urls import path
from . import views
urlpatterns = [
    path('register-passenger' ,views.register_passenger , name = 'register-passenger' ),
    path('register-driver' ,views.register_driver , name = 'register-driver' ),
    path('login-driver' ,views.login_driver , name = 'login-driver' ),
    path('login-passenger' ,views.login_passenger , name = 'login-passenger' ),
    path('logout' ,views.logout_view , name = 'logout' ),

]