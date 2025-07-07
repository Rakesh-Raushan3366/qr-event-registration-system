from django.contrib import admin # type: ignore
from django.db import models
from akhilbhartiye.models import *

# Register your models here.

@admin.register(AkhilBhartiyaRegistration)
class AkhilBhartiyaRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'daytib', 'gatividhi', 'daytib_chetra_adhikari', 'chetra', 'prant', 'arrival_flight_number', 
        'arrival_train_number', 'departure_flight_number', 'departure_train_number', 'created_at']
