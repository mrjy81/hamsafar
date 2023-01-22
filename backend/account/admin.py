from django.contrib import admin
from .models import (
    Driver ,
    Phones,
    Users ,
    Client,
)
from django.contrib.auth.admin import UserAdmin

@admin.register(Users)
class CustomUser(UserAdmin):
    model = Users 
    
admin.site.register(Driver)
admin.site.register(Phones)
admin.site.register(Client)
