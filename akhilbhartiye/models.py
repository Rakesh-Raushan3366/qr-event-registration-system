from django.db import models

# Create your models here.

class AkhilBhartiyaRegistration(models.Model):

    id = models.AutoField(primary_key=True)
    # Personal Info
    name = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    daytib = models.TextField(blank=True, null=True)
    gatividhi = models.TextField(blank=True, null=True)
    daytib_chetra_adhikari = models.TextField(blank=True, null=True)
    chetra = models.TextField(blank=True, null=True)
    prant = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    vividhDaytiva = models.TextField(blank=True, null=True)

    # Arrival - Flight
    arrivalMode = models.TextField(blank=True, null=True)
    arrival_flight_number = models.TextField(blank=True, null=True)
    arrival_airport_terminal = models.TextField(blank=True, null=True)
    arrival_flight_date = models.TextField(blank=True, null=True)
    arrival_flight_time = models.TextField(blank=True, null=True)

    # Arrival - Train
    arrival_train_number = models.TextField(blank=True, null=True)
    arrival_train_coach = models.TextField(blank=True, null=True)
    # arrival_pnr = models.TextField(blank=True, null=True)
    arrival_station = models.TextField(blank=True, null=True)
    arrival_train_date = models.TextField(blank=True, null=True)
    arrival_train_time = models.TextField(blank=True, null=True)

    # Arrival - Road
    # arrival_bus_operator = models.TextField(blank=True, null=True)
    arrival_bus_station = models.TextField(blank=True, null=True)
    arrival_bus_date = models.TextField(blank=True, null=True)
    # arrival_bus_time = models.TextField(blank=True, null=True)

    # Arrival - Self Vehicle
    arrival_vehicle_number = models.TextField(blank=True, null=True)
    arrival_selfVehicle_date = models.TextField(blank=True, null=True)
    # arrival_selfVehicle_time = models.TextField(blank=True, null=True)

    # Departure - Flight
    departureMode = models.TextField(blank=True, null=True)
    departure_flight_number = models.TextField(blank=True, null=True)
    departure_airport_terminal = models.TextField(blank=True, null=True)
    departure_flight_date = models.TextField(blank=True, null=True)
    departure_flight_time = models.TextField(blank=True, null=True)

    # Departure - Train
    departure_train_number = models.TextField(blank=True, null=True)
    departure_train_coach = models.TextField(blank=True, null=True)
    # departure_pnr = models.TextField(blank=True, null=True)
    departure_station = models.TextField(blank=True, null=True)
    departure_train_date = models.TextField(blank=True, null=True)
    departure_train_time = models.TextField(blank=True, null=True)

    # Departure - Road
    # departure_bus_operator = models.TextField(blank=True, null=True)
    bus_boarding_from = models.TextField(blank=True, null=True)
    departure_bus_date = models.TextField(blank=True, null=True)
    # departure_bus_time = models.TextField(blank=True, null=True)

    # Departure - Self Vehicle
    departure_vehicle_number = models.TextField(blank=True, null=True)
    departure_selfVehicle_date = models.TextField(blank=True, null=True)
    # departure_selfVehicle_time = models.TextField(blank=True, null=True)

    # Other Info
    other_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'akhil_bhartiya_registration'

class PrantMaster(models.Model):
    prant_id = models.AutoField(primary_key=True)
    prant_name = models.CharField(max_length=255, null=True, blank=True)
    prant_hindi = models.CharField(max_length=255, null=True, blank=True)
    chetra_id = models.ForeignKey('ChetraMaster', models.DO_NOTHING, db_column='chetra_id', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'prant_master'

class ChetraMaster(models.Model):
    chetra_id = models.AutoField(primary_key=True)
    chetra_name = models.CharField(max_length=255, null=True, blank=True)
    chetra_hindi = models.CharField(max_length=255, null=True, blank=True)
    akhil_bhartiya_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chetra_master'
